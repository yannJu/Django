## 💫Form💫
- ### 질문 등록 버튼 만들기
  - `Form`을 이용하여 입력받기
  - *[./yannjuApp/forms.py](./yannjuApp/forms.py)* 에 class를 작성하고 `Question 객체`와 연결
   
    ```python
    //yannjuApp/forms.py
    class QuestionForm(forms.ModelForm):
        #Model에 대한것을 입력받아야하므로 Model에 대해 맞추겠다
        class Meta: #설명하는 데이터
            model  = Question
            fields = ['subject', 'content'] #진짜 연계를 시킬 데이터 -> id, date는 연계 X
    ``` 
  - `django`가 *field를* 이용하여 Question 객체와 **Mapping**시킴 
  - `질문등록`버튼을 클릭하면 다음과 같은 화면으로 넘어가게 된다.
   
   ![질문등록 화면](../img/5_img(1).png)
   - `question/create` 화면으로 넘어갈때는 **GET** 메소드로 넘어가게 된다.
     - 해당화면에서 `저장하기` 버튼을 눌렀을 때는 **POST**로 넘어가고, 해당 화면은 **GET, POST** 둘다 받게 됨
     - 각 기능에 따라 *다르게* 처리해야한다.
- ### 같은 URL에서 다른 기능 처리
  ```python
  //yannjuApp/views.py
  def question_create(request):
    """
    yannjuApp 질문등록
    """
    if request.method == 'POST': #POST 요청이라면 -> 저장하기 버튼
        form = QuestionForm(request.POST) #request.POST : 사전 형태로 데이터가 들어옴
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('yannjuName:index')
    else: #GET 요청이라면 -> 질문등록버튼
        form = QuestionForm() #비어있는 데이터
    return render(request, 'yannjuApp/question_form.html', {'form':form})
  ```  
    - `request.method` 를 이용하여 **POST** 와 **GET**을 구분하여 기능을 나누어줌
    - `GET`요청인 경우 비어있는 `QuestionForm()`을 만들어줌
    - `POST`요청인 경우 데이터가 포함된 `QuestionForm()`을 **DB**에 저장
    - *question/create* 주소에서 내용을 작성 후 `저장하기`를 클릭하면 목록에 데이터가 뜸
     
        ![저장 후 목록](../img/5_img(2).png)
- ### Form에 부트스트랩 적용
    - *[./yannjuApp/forms.py](./yannjuApp/forms.py)* 에서 각 field들을 추가적으로 관리
     
        ```html
        <!--yannjuApp/forms.py-->
        <!--상위 생략-->
         widgets = {
            'subject' : forms.TextInput(attrs={'class':'form-control'}),
            'content' : forms.Textarea(attrs={'class' : 'form-control', 'rows' : 10}),
        }
        <!--하위 생략-->
        ``` 
    -  `Widget` : 사전형태로 이루어져 각 content를 관리
- ### 직접 `<div>`로 정의하여 관리
   - *[./templates/yannjuApp/question_form.html](./templates/yannjuApp/question_form.html)* 에서 수작업으로 form을 작성하여 관리
   - 이때 `as_p`로 `<p>`태그로 묶은것을 *해제* 해야함
    
        ``` html
        <!--templates/yannjuApp/question_form.html-->
        <!--상위 생략-->
        <form method="post" class="post-form my-3">
            {% csrf_token %}
            <!--<p>태그로 묶은 것을 해제-->
            {% comment %} {{form.as_p}} <!--as_p : <p>태그로 묶어서 입력을 보내겠다는 의미--> {% endcomment %}
            
                <!--Err Start-->
                <!--Err End-->
                <div class="form-group">
                    <label for="subject">제목</label>
                    <input type="text" class="form-control" name="subject" 
                    id="subject" value="{{ form.subject.value|default_if_none:'' }}">
                </div>
                <div class="form-group">
                <label for="content">내용</label>
                <textarea class="form-control" name="content" id="content" 
                rows="10">{{form.content.value|default_if_none:''}}</textarea>
                </div>
        <!--하위 생략-->
        ```
    - **직접** 각 컨텐츠들을 작성하여 화면에 표시