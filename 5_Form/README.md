## ๐ซForm๐ซ
- ### ์ง๋ฌธ ๋ฑ๋ก ๋ฒํผ ๋ง๋ค๊ธฐ
  - `Form`์ ์ด์ฉํ์ฌ ์๋ ฅ๋ฐ๊ธฐ
  - *[./yannjuApp/forms.py](./yannjuApp/forms.py)* ์ class๋ฅผ ์์ฑํ๊ณ  `Question ๊ฐ์ฒด`์ ์ฐ๊ฒฐ
   
    ```python
    //yannjuApp/forms.py
    class QuestionForm(forms.ModelForm):
        #Model์ ๋ํ๊ฒ์ ์๋ ฅ๋ฐ์์ผํ๋ฏ๋ก Model์ ๋ํด ๋ง์ถ๊ฒ ๋ค
        class Meta: #์ค๋ชํ๋ ๋ฐ์ดํฐ
            model  = Question
            fields = ['subject', 'content'] #์ง์ง ์ฐ๊ณ๋ฅผ ์ํฌ ๋ฐ์ดํฐ -> id, date๋ ์ฐ๊ณ X
    ``` 
  - `django`๊ฐ *field๋ฅผ* ์ด์ฉํ์ฌ Question ๊ฐ์ฒด์ **Mapping**์ํด 
  - `์ง๋ฌธ๋ฑ๋ก`๋ฒํผ์ ํด๋ฆญํ๋ฉด ๋ค์๊ณผ ๊ฐ์ ํ๋ฉด์ผ๋ก ๋์ด๊ฐ๊ฒ ๋๋ค.
   
   ![์ง๋ฌธ๋ฑ๋ก ํ๋ฉด](../img/5_img(1).png)
   - `question/create` ํ๋ฉด์ผ๋ก ๋์ด๊ฐ๋๋ **GET** ๋ฉ์๋๋ก ๋์ด๊ฐ๊ฒ ๋๋ค.
     - ํด๋นํ๋ฉด์์ `์ ์ฅํ๊ธฐ` ๋ฒํผ์ ๋๋ ์ ๋๋ **POST**๋ก ๋์ด๊ฐ๊ณ , ํด๋น ํ๋ฉด์ **GET, POST** ๋๋ค ๋ฐ๊ฒ ๋จ
     - ๊ฐ ๊ธฐ๋ฅ์ ๋ฐ๋ผ *๋ค๋ฅด๊ฒ* ์ฒ๋ฆฌํด์ผํ๋ค.
- ### ๊ฐ์ URL์์ ๋ค๋ฅธ ๊ธฐ๋ฅ ์ฒ๋ฆฌ
  ```python
  //yannjuApp/views.py
  def question_create(request):
    """
    yannjuApp ์ง๋ฌธ๋ฑ๋ก
    """
    if request.method == 'POST': #POST ์์ฒญ์ด๋ผ๋ฉด -> ์ ์ฅํ๊ธฐ ๋ฒํผ
        form = QuestionForm(request.POST) #request.POST : ์ฌ์  ํํ๋ก ๋ฐ์ดํฐ๊ฐ ๋ค์ด์ด
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('yannjuName:index')
    else: #GET ์์ฒญ์ด๋ผ๋ฉด -> ์ง๋ฌธ๋ฑ๋ก๋ฒํผ
        form = QuestionForm() #๋น์ด์๋ ๋ฐ์ดํฐ
    return render(request, 'yannjuApp/question_form.html', {'form':form})
  ```  
    - `request.method` ๋ฅผ ์ด์ฉํ์ฌ **POST** ์ **GET**์ ๊ตฌ๋ถํ์ฌ ๊ธฐ๋ฅ์ ๋๋์ด์ค
    - `GET`์์ฒญ์ธ ๊ฒฝ์ฐ ๋น์ด์๋ `QuestionForm()`์ ๋ง๋ค์ด์ค
    - `POST`์์ฒญ์ธ ๊ฒฝ์ฐ ๋ฐ์ดํฐ๊ฐ ํฌํจ๋ `QuestionForm()`์ **DB**์ ์ ์ฅ
    - *question/create* ์ฃผ์์์ ๋ด์ฉ์ ์์ฑ ํ `์ ์ฅํ๊ธฐ`๋ฅผ ํด๋ฆญํ๋ฉด ๋ชฉ๋ก์ ๋ฐ์ดํฐ๊ฐ ๋ธ
     
        ![์ ์ฅ ํ ๋ชฉ๋ก](../img/5_img(2).png)
- ### Form์ ๋ถํธ์คํธ๋ฉ ์ ์ฉ
    - *[./yannjuApp/forms.py](./yannjuApp/forms.py)* ์์ ๊ฐ field๋ค์ ์ถ๊ฐ์ ์ผ๋ก ๊ด๋ฆฌ
     
        ```html
        <!--yannjuApp/forms.py-->
        <!--์์ ์๋ต-->
         widgets = {
            'subject' : forms.TextInput(attrs={'class':'form-control'}),
            'content' : forms.Textarea(attrs={'class' : 'form-control', 'rows' : 10}),
        }
        <!--ํ์ ์๋ต-->
        ``` 
    -  `Widget` : ์ฌ์ ํํ๋ก ์ด๋ฃจ์ด์ ธ ๊ฐ content๋ฅผ ๊ด๋ฆฌ
- ### ์ง์  `<div>`๋ก ์ ์ํ์ฌ ๊ด๋ฆฌ
   - *[./templates/yannjuApp/question_form.html](./templates/yannjuApp/question_form.html)* ์์ ์์์์ผ๋ก form์ ์์ฑํ์ฌ ๊ด๋ฆฌ
   - ์ด๋ `as_p`๋ก `<p>`ํ๊ทธ๋ก ๋ฌถ์๊ฒ์ *ํด์ * ํด์ผํจ
    
        ``` html
        <!--templates/yannjuApp/question_form.html-->
        <!--์์ ์๋ต-->
        <form method="post" class="post-form my-3">
            {% csrf_token %}
            <!--<p>ํ๊ทธ๋ก ๋ฌถ์ ๊ฒ์ ํด์ -->
            {% comment %} {{form.as_p}} <!--as_p : <p>ํ๊ทธ๋ก ๋ฌถ์ด์ ์๋ ฅ์ ๋ณด๋ด๊ฒ ๋ค๋ ์๋ฏธ--> {% endcomment %}
            
                <!--Err Start-->
                <!--Err End-->
                <div class="form-group">
                    <label for="subject">์ ๋ชฉ</label>
                    <input type="text" class="form-control" name="subject" 
                    id="subject" value="{{ form.subject.value|default_if_none:'' }}">
                </div>
                <div class="form-group">
                <label for="content">๋ด์ฉ</label>
                <textarea class="form-control" name="content" id="content" 
                rows="10">{{form.content.value|default_if_none:''}}</textarea>
                </div>
        <!--ํ์ ์๋ต-->
        ```
    - **์ง์ ** ๊ฐ ์ปจํ์ธ ๋ค์ ์์ฑํ์ฌ ํ๋ฉด์ ํ์
- ### ์๋ฌ์ฒ๋ฆฌ
  - `form_isvalid()` ์ฌ์ฉ์ **False** ์ ๊ฒฝ์ฐ ์ค๋ฅ ์ฒ๋ฆฌ๋ฅผ ํด์ผํจ
    - **False** ๋ฐ์์ `form.errors`๊ฐ ๋ฐํ๋จ
  - BootStrap ์์ `Alert`๋ฅผ ์ฌ์ฉ
   
    ```html
    <!--Err Start-->
    {% if form.errors %}
        <div class="alert alert-danger" role ='alert'>
            {% for field in form %}
                {% if  field.errors %}
                    <strong>{{ field.label }}</strong> 
                    {{ field.errors }}
                {% endif %}
            {% endfor %}
            </div>
    {% endif %}
    <!--Err End-->
    ``` 
    - field.error**s** : ์ฌ๋ฌ๊ฐ์ ์๋ฌ๊ฐ *๋์์* ์๋ฐฐ๋  ์ ์์
     
    ![](../img/5_img(3).png) 
  - ์๋ฌด๊ฒ๋ *์์ฑํ์ง ์์* **์ค๋ฅ๊ฐ** ๋ฐ์ํ ๊ฒ์ ๋ณผ ์ ์์
  - ๊ฐ ํญ๋ชฉ๋ณ๋ก **ํญ๋ชฉ ์๋**์ ์ค๋ฅ๋ฅผ ํ๊ธฐํ๋ ค๋ฉด ์ ์ฒด `loop`๋ฅผ ๋๋ ๊ฒ์ด ์๋๋ผ ๊ฐ๊ฐ `loop`๋ฅผ ๋๋ฉด ๋จ
   
    ```html
    <!--TITLE-->
    <div class="form-group">
        <label for="subject">์ ๋ชฉ</label>
        <input type="text" class="form-control" name="subject" 
        id="subject" value="{{ form.subject.value|default_if_none:'' }}">
        <!--ํญ๋ชฉ๋ณ ์๋ฌ์ฒ๋ฆฌ-->
        {% if form.subject.errors %}
            <div class="text-danger" >
                {% for error in form.content.errors %}
                    <div>
                            <i class = 'fa-solid fa-triangle-exclamation'></i>
                            {{error}}
                    </div>
                {% endfor %}
        {% endif %}
        <!--์๋ฌ์ฒ๋ฆฌ ๋-->
    </div>
    ``` 
    - `subject`์ ๋ํ `Error`๋ค์ ๊ฐ๊ฐ ์ฒ๋ฆฌํด์ ์นธ ์๋์ ๋ํ๋
  - `subject`์ `content` ๋ชจ๋ ์ ์ฉํ๋ฉด ์๋์ ๊ฐ์
   
    ![์๋ฌ์ด๋ฏธ์ง2](../img/5_img(4).png)
 - ํฐํธ ์ ์ฉ
   - [fonts.google.com](https://fonts.google.com/) ๋ฅผ ํตํด **ํฐํธ ์ค์ ** ๊ฐ๋ฅ
   - *[./static/style.css](./static/style.css)* ์ ์ ํํ font๋ฅผ ์ถ๊ฐ
    
        ```css
        @import url('https://fonts.googleapis.com/css2?family=Poor+Story&display=swap');
        * {
        font-family: 'Poor Story', cursive;
        }
        ``` 
    - ํฐํธ๋ฅผ *select* ํ๊ณ  `import`์ฝ๋์ `font-familt` ์ฝ๋๋ฅผ **๋ณต์ฌ**
    - ์๋์ ๊ฐ์ ๊ฒฐ๊ณผ๋ฅผ ์ป์
     
        ![ํฐํธ์ค์ ](../img/5_img(5).png) 