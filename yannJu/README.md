## ๐Final Application๐
### `yannJu`
---
- ### ํ์๊ด๋ฆฌ ์ฑ ์ถ๊ฐ
  - `django-admin startapp` ๋ช๋ น์ด๋ฅผ ์ด์ฉํ์ฌ **common** ์ด๋ผ๋ app์ ์ถ๊ฐ
  - *[./config/settings.py > INSTALLED_APPS](./config/settings.py)* ์ `App` ์ ๊ทผ์ ์ํด `common` ์ ์ถ๊ฐ
  - `auth`๋ฅผ ์ด์ฉํ๋๋ฐ ์ฃผ๋ก `CBV ` ์ฆ **ํด๋์ค** ๊ธฐ์ค์ผ๋ก ๊ด๋ฆฌ
- ### ๋ก๊ทธ์ธ ์ ์  ๋์ ์ผ๋ก ๊ด๋ฆฌ
  - **Login**
    - *[templates/navbar.html](templates/navbar.html)* ์ *๋ก๊ทธ์ธ ์ฃผ์*๋ก ์ด๋ํ  ์ ์๋๋ก ์์ 
    - *๋ก๊ทธ์ธ์ฃผ์* ๋ ์์์ ์๋ก ์ถ๊ฐํ `common` ์ฑ์์ ๊ด๋ฆฌ
    - *[./common/urls.py](./common/urls.py)*  ์์ `๋ก๊ทธ์ธ ์ฃผ์` URL์ ์ถ๊ฐ
     
        ```python
        //./common/urls.py
        //<์์์๋ต>
        path('login', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
        //<ํ์์๋ต>
        ```
    - `LoginView`๋ฅผ ์ด์ฉํ์ฌ *Login ๊ด๋ฆฌ* ๋ฅผ ๋ณด๋ค ํธํ๊ฒ ์ด์ฉํ  ์ ์์
    - ๋ก๊ทธ์ธ URL๋ก ์ด๋ํ๊ธฐ ์ํด `template_name`์ ํ ๋น
    - ์ดํ **๋ก๊ทธ์ธ ํํ๋ฆฟ** ์ ์ (*[./templates/common/login.html](./templates/common/login.html)*) ๋ฐ ์๋ฌ์ฒ๋ฆฌ
    - ์๋ฌ์ฒ๋ฆฌ๋ `{% include "form_errors.html" %}` ๋ฅผ ์ถ๊ฐํ์ฌ *[./templates/form_errors.html](./templates/form_errors.html)* ์์ ๋ก๊ทธ์ธ ์๋ฌ๋ฅผ ์ฒ๋ฆฌ
     
    ![์ค๋ฅ1](../img/img1.png)|![์ค๋ฅ2](../img/img2.png)
    --- | --- | 
  - **Logout**
    - *[templates/navbar.html](templates/navbar.html)* ์ ๋ก๊ทธ์ธ๊ณผ ๋์ผํ๊ฒ ์ถ๊ฐ
    - ๋จ **๋ก๊ทธ์ธ ์ํ**๋ฅผ ํ์ธํด์ผํจ
     
        ```html
        <!--templates/navbar.html--d>
        {% if user.is_authenticated %}
                <li class="nav-item ">
                    <a class="nav-link" href = '#'> {{user.username}} ๋ เธสโขอกฬซโขสเธ ๋ฐ๊ฐ์ต๋๋ค !</a>                   
                </li>
                <li class="nav-item ">
                    <a  class="nav-link" href="{% url 'common:logout' %}">
                        <i class="fa-solid fa-right-to-bracket"></i>
                        ๋ก๊ทธ์์
                    </a>                   
                </li>
            {% else %}
                <li class="nav-item ">
                    <a  class="nav-link" href="{% url 'common:login' %}">๋ก๊ทธ์ธํ๊ธฐ .______.</a>                   
                </li>
            {% endif %}
        ``` 
        - `is_authenticated` ๋ฅผ ์ด์ฉํ์ฌ `true`๋ผ๋ฉด ๋ก๊ทธ์ธ ์ํ์ด๋ฏ๋ก **๋ก๊ทธ์์ ๋ฒํผ**์ ๋์์ค๋ค.
        - `false` ์ธ ๊ฒฝ์ฐ ๋ก๊ทธ์์ ์ํ ์ด๋ฏ๋ก **๋ก๊ทธ์ธ ๋ฒํผ** ์ ๋์์ค๋ค.
         
        ![](../img/img3.PNG)
        ![](../img/img4.PNG)
      - ๋ก๊ทธ์์์ ์ฑ๊ณตํ๊ฒ ๋๋ฉด **์ด๊ธฐํ๋ฉด์ผ๋ก** ๋์๊ฐ๋๋ก ํ๋ค.
- ### ์ ์ ์ด๋ฏธ์ง ๋๋คํ๊ฒ ์ ๊ณต [(randomuser.me)](http://www.randomuser.me) ๊ฐ๋ฅ
- ### ํ์๊ฐ์ ๊ธฐ๋ฅ ์ถ๊ฐ
  - *์ ํจ์ฑ ๊ฒ์ฌ* ๋ฐ Primary Key ๋ฅผ ์ฒดํฌ *(์ค๋ณต๊ฒ์ฌ)* ํด์ผํจ
  - `django.contrib.auth ` ์์ **ํ์๊ด๋ฆฌ** ๊ธฐ๋ฅ์ ์ ๊ณต
  - *[./templates/common/login.html](./templates/common/login.html)* ์ Login ํค๋ ์์ `ํ์๊ฐ์` ๋ฒํผ์ ์์ฑ โ **Grid** ๋ฅผ ๋ถํธ์คํธ๋ฉ์ ์ด์ฉํ์ฌ ์ ์ฉ

    ![ํ์๊ฐ์ ๋ฒํผ ์์ฑ](../img/img_%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%20%EB%B2%84%ED%8A%BC.PNG)
  - *[./common/urls.py](./common/urls.py)*์ ๋ค์๊ณผ ๊ฐ์ด `signup` URL์ *mapping*
   
    ```python
    //./common/urls.py
    //(... ์๋ต ...)
    from . import views
    //(... ์๋ต ...)
    urlpatterns = [
    //(... ์๋ต ...)
    path('signup/', views.signup, name='signup'),
        ]
    ```
  - **Form** ๋ง๋ค๊ธฐ
    - *[./common/forms.py](./common/forms.py)* ํ์ผ์ `UserForm`์ด๋ผ๋ form์ ์์ฑ
     
        ```python
        //./common/forms.py
        from django import forms
        from django.contrib.auth.forms import UserCreationForm
        from django.contrib.auth.models import User

        class UserForm(UserCreationForm):
            email = forms.EmailField(label='์ด๋ฉ์ผ')
            
            class Meta:
                model = User
                fields = ('username', 'email')
        ``` 
        - email๊ณผ ๊ฐ์ด **์ฌ์ ์**ํ  ์ ์์
  - Signup **Template** ๋ง๋ค๊ธฐ
    - *[./templates/common/signup.html](./templates/common/signup.html)* ์ ์ฌ์ฉ์์ด๋ฆ, ๋น๋ฐ๋ฒํธ, ์ด๋ฉ์ผ ์๋ ฅ์ ๋ฐ์ ์ ์๋๋ก *Template* ์์ฑ
    - `as_p`๋ก ๋ฌถ์ด ์์ฑํ  ์ ์์ง๋ง, ๋ณด๋ค ๊ฐ์์ฑ์ ๋์ด๊ธฐ ์ํด `field` ๊ฐ๊ฐ ์์ฑ

    ![ํ์๊ฐ์์ฐฝ](../img/img_%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%20%ED%8E%98%EC%9D%B4%EC%A7%80.PNG)
  - `AUTH_PASSWORD_VALIDATORS` ๋ก ์ธํด ๋ณด๋ค *๋ณต์กํ๊ฒ* Passwd๋ฅผ ๊ด๋ฆฌํ  ์ ์์
  - *[./common/views.py](./common/views.py)*
   
    ```python
    //./common/views.py
    //(์๋ต..)
    if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
    //(์๋ต..)
    ```
    - `authenticate` : user ์ด๋ฆ์ ์ฒดํนํ๊ณ ์๋ค๋ฉด ๋น๋ฐ๋ฒํธ ์ผ์น๋ฅผ ํ์ธ
      - user name : **O**, pwd : **O** โ user๊ฐ์ฒด **์์ฑ**
      - user name : **X** ์ด๊ฑฐ๋ pwd : **X**  โ **None** ์๋ฐํ
    - `login` ์ ๊ฑฐ์น ํ ํ์ *์์ฑ*
- ### ํ์๊ฐ์ ์๋ฌ ์ฒ๋ฆฌ
  - **Login/Logout**  ๊ณผ ๋์ผํ๊ฒ *[form_errors.html](./templates/form_errors.html)* ์ ์ฐ๋์ํด

    ![](../img/img_errTest.png) 
- ### ํ์๊ฐ์ ๋ฐ ๋ก๊ทธ์ธ ํ์คํธ
  - ํ์๊ฐ์ ์ฐฝ์์ *์ ๋ณด* ์๋ ฅ   
   
    ![ํ์๊ฐ์](../img/img_%EB%A1%9C%EA%B7%B8%EC%9D%B8%EA%B3%BC%EC%A0%95.PNG) |![ํ์๊ฐ์ ํ ๋ก๊ทธ์ธ](../img/img_%EB%A1%9C%EA%B7%B8%EC%9D%B8%EC%84%B1%EA%B3%B51.PNG)
    ---|---|
  - ๋ก๊ทธ์ธ ์ฐฝ์์ *๋ก๊ทธ์ธ* 

    ![๋ก๊ทธ์ธ](../img/img_%EB%A1%9C%EA%B7%B8%EC%9D%B8.PNG)|![๋ก๊ทธ์ธํ ๊ฒฐ๊ณผ](../img/img_%EB%A1%9C%EA%B7%B8%EC%9D%B8%EC%84%B1%EA%B3%B52.PNG)
    ---|---|
- ### ๋ก๊ทธ์ธ ๋ฒํผ ์์น ๋ณ๊ฒฝ
  - ๋ก๊ทธ์ธ ํค๋์ ๊ฐ์ ๋ผ์ธ์ ์๋ ์์น๋ฅผ  ๋ณ๊ฒฝ
  - ๋ก๊ทธ์ธ **๋ฒํผ** ์๋์ ํ์๊ฐ์ ๋ฒํผ *์ถ๊ฐ*

  ![๋ก๊ทธ์ธ ๋ฒํผ ์์น ๋ณ๊ฒฝ](../img/img_%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85ver2.PNG) 
- ### ๊ฒ์๊ธ ๊ฐ๊ฐ์ ํ์ฉ ๋ฒ์ ์ค์ 
  - ๊ฒ์๊ธ *์์ฑ์* ์ถ๊ฐํ๊ธฐ
    - `Question` ๊ฐ์ฒด์ `User`๊ฐ์ฒด๋ฅผ **Join**
      - *[./yannjuApp/models.py > Question](./yannjuApp/models.py)* ์ *auth* ์ถ๊ฐ
       
        ```python
        // ./yannjuApp/models.py
        from django.contrib.auth.models import User
        //(์๋ต . .)
        auth = models.ForeignKey(User, on_delete=models.CASCADE)
        //(์๋ต . .)
        ``` 
    - ๊ฐ์ฒด์ *ํ๋*๋ฅผ ์ถ๊ฐ ํ ํ `migration`์ ํด ์ฃผ์ด์ผํจ
    - ์ด๋ *ํ๋*๊ฐ ์ถ๊ฐ๋๋ฉด์ **ํ์ด๋ธ ๊ตฌ์กฐ**๊ฐ ๋ฐ๋ ์ํ์์๋ ๊ธฐ์กด ๋ฐ์ดํฐ์๋ *์ ์ฉ*์ ์์ผ์ฃผ์ด์ผํจ
    - ํ์ง๋ง `author`๋ **Not Null** ์ด๋ฏ๋ก default ๊ฐ์ด ์ง์  ๋์ด์ผํจ
      - `python manage.py makemigrations`๋ฅผ ํ๊ฒ ๋๋ฉด ํด๋น ๋ถ๋ถ์ ๋ํ **๊ฒฝ๊ณ ** ๋ฐ์
      - default ๊ฐ์ ์ ํด์ฃผ๊ณ  `python manage.py migrate`๋ฅผ ์คํ์์ผ DB์ ์ ์ฉ
      - ๋ค์๊ณผ ๊ฐ์ด *[./yannjuApp/migrations/0002_question_auth.py](./yannjuApp/migrations/0002_question_auth.py)* ํ์ผ์ด ์์ฑ๋๋ฉฐ ์์ฑ๋จ

        ```python
        //./yannjuApp/migrations/0002_question_auth.py
        //(์๋ต. .)
        operations = [
            migrations.AddField(
                model_name='question',
                name='auth',
                field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
                preserve_default=False,
            ),
        //(์๋ต. .)
        ]
        ```
    - `Answer` ๊ฐ์ฒด์๋ ๋์ผํ๊ฒ ์ ์ฉ
  - **๋ก๊ทธ์ธ ๊ณ์ **๋ง ๊ฒ์๊ธ์ *์์ฑ*
- ### ์์  ์ฒ๋ฆฌ
  - ๊ฒ์๊ธ **์์ฑ์** ๋ง ๊ฒ์๊ธ์ ์์ 
  - ์ค๋ฅ์ฒ๋ฆฌ -> ๋ฒ์ฉ์ฒ๋ฆฌ
  - *[./templates/yannjuApp/question_form.html](./templates/yannjuApp/question_form.html)*, *[./templates/yannjuApp/answer_form.html](./templates/yannjuApp/answer_form.html)* ๊ณผ ๊ฐ์ด `form` ์์ฑ
  - ์ดํ ๊ฐ `Question`, `Answer` ์ ๋ถ๋ฌ์จ ํ `Form` ๊ฐ์ฒด ์ด์ฉํ์ฌ ์์ฑ
  -  `save()` ๋ฅผ ์ด์ฉํ์ฌ ๋ฎ์ด์์ฐ๊ธฐ
- ### ์ญ์  ์ฒ๋ฆฌ `(V0.0.2-)`
  - ๋ฐ๋ก **์ญ์ ** ๋๋ ๊ฒ์ ๋ฐฉ์ง ํ๊ธฐ ์ํด ํ๋ฒ ๋ ๋ฌป๋ ์ฐฝ์ ๋์
  - *[./templates/yannjuApp/question_detail.html](./templates/yannjuApp/question_detail.html)* ์ `์ญ์ ` ๋ฒํผ ์ถ๊ฐ
    - ์ด ๋ `bt4` ์ ๋ฒํผ ํด๋์ค๊ฐ ์๋ **script** ์ฌ์ฉ ์ผ๋ก *๋์  ์ฒ๋ฆฌ* ์งํ
  - `data-uri`: ๋ธ๋ผ์ฐ์ ๋ ์์ฑ์ ๋ชจ๋ฆ, ๊ฐ๋ฐ์๋ง ์๊ณ  ์ ๋ณด๋ฅผ ๋ด๊ธฐ๋ง ํจ **'data-'** ๋ก ์์ํ๋ฉด ์ฌ์ฉ์ ์ ์ ์์ฑ : script ์ฒ๋ฆฌ๋ฅผ ํด์ผํจ
  - *[base.html](./templates/base.html)* ์ script block ์ถ๊ฐ
   
   ```html
  <!--./templates/base.html-->
  <!--์๋ต . .25-26๋ฒ์ค-->
  <!-- Delete -->
  {% block script %}{% endblock script %}
  <!--์๋ต . .-->
   ```
  - *[./templates/yannjuApp/question_detail.html](./templates/yannjuApp/question_detail.html)* ์ `<script>` ๋ธ๋ก์ ๋ง๋ค๊ณ  ๋์ ์ฒ๋ฆฌ๋ฅผ ์งํ

  ```html
  <!--./templates/yannjuApp/question_detail.html-->
  <!--์๋ต..-->
  {% block script %}
  <script>
      $(document).ready(function(){
          $(".delete").on("click", function() {
              if (confirm("์ ๋ง๋ก ์ญ์  ํ์๊ฒ ์ต๋๊น?")) {
                  location.href = $(this).data('uri');
              }
          });
      });
  </script>
  {% endblock script %}
  ``` 
  - `script function`์ ์ด์ฉํ์ฌ ํด๋น ํ์ด์ง๊ฐ ์ค๋น๋๊ณ , **delete** ํด๋์ค๊ฐ **click** ๋ ๊ฒฝ์ฐ `if`๋ฌธ ์คํ
  - *[./yannjuApp/urls.py](./yannjuApp/urls.py)*์ **delete** ์ฃผ์๋ฅผ mapping
  - *[./yannjuApp/views.py](./yannjuApp/views.py)* ์ ๊ธฐ๋ฅ์ ์์ฑ

    ![์ญ์ img](../img/v2_img(1).PNG)
    ![์ญ์ img](../img/v2_img(2).PNG)
    ![์ญ์ img](../img/v2_img(3).PNG)

- ### ๋ต๋ณ ์์  ๋ฐ ์ญ์ ํ๊ธฐ `(V0.0.2-)`
  - *์ง๋ฌธ ์์  ๋ฐ ์ญ์ * ์ **์ ์ฌํ๊ฒ** ์งํ
  - *[./templates/yannjuApp/question_detail.html](./templates/yannjuApp/question_detail.html)* ์ ๋ต๋ณ ๋ถ๋ถ์ `์์ `, `์ญ์ ` ๋ฒํผ ์์ฑ
   
    ![๋ต๋ณ ์์ , ์ญ์  ๋ฒํผ ์์ฑ](../img/v2_img(5).PNG)
  - ๊ฐ ๋ฒํผ ๋น `url`์ ์ค์ ํ์ฌ mapping
  - *[./yannjuApp/views.py](./yannjuApp/views.py)* ์ ๊ธฐ๋ฅ์ ์ฒ๋ฆฌํ๋ ํจ์๋ฅผ ๊ตฌํ
    - ์์  : *[./templates/yannjuApp/answer_form.html](./templates/yannjuApp/answer_form.html)* ์ ์ด์ฉํ์ฌ ์ฌ์์ฑ ํ `save`
    - ์ญ์  : ์ง๋ฌธ ์ญ์ ์ ์ ์ฌํ๊ฒ `script`๋ฅผ ํตํด ์ญ์ ์ฌ๋ถ ๋ค์ ๋ฌป๊ธฐ
- ### Bootstrap Form ์ด์ฉํ๊ธฐ
  - ๊ธฐ์กด์ `๋ก๊ทธ์ธ` form ์ด ์๋ **Bootstrap** ์์ ์ ๊ณตํ๋ Form ์ ํตํด ํํ๋ฆฟ ๊ตฌ์ฑ
  - *[./config/settings.py](./config/settings.py)* ์ `INSTALLED_APPS` ์ **'bootstrap4'** ์ ์ถ๊ฐ
  - ์ดํ `bootstrap` form์ ์ฌ์ฉํ  ๊ฒฝ์ฐ `load` ๋ฐ ๋ถ๋ฌ์ค๊ธฐ
   
    ```html
    <!--./templates/yannjuApp/answer_form.html-->
    {% extends 'base.html' %}
    {% load bootstrap4 %}

    {% block content %}
    <form method="POST" class='post-form'>
        {% csrf_token %}
        {% bootstrap_form form %}

        <button type='submit' class="btn btn-primary"> ์ ์ฅํ๊ธฐ </button>
    </form>
    {% endblock content %}
    ```
    - ์๋จ์ `load`๋ฅผ ํตํด **bootstrap** ์ ๋ถ๋ฌ์จ ํ ์ค๊ฐ์ `{% bootstrap_form form %}` form ์ฌ์ฉ
    - *[./templates/common/signup.html](./templates/common/signup.html)* ์ ๊ธฐ์กด ์์ฑํ๋ ์์ฑ๋ค์ ์ง์ฐ๊ณ  ์์ฒ๋ผ `{% bootstrap_form form %}` form ์์ฑ

    ![๋ถํธ์คํธ๋ฉ ํผ ์ฌ์ฉ](../img/v2_img(4).PNG)
  - `๋ก๊ทธ์ธ, ๋ต๋ณ์์ ` ๋ฑ์๋ ๋์ผํ๊ฒ *์ ์ฉ*
- ### ๊ฒ์๊ธ ๋๊ธ๊ธฐ๋ฅ ์ถ๊ฐ`(V0.0.2-)`
  - `DB`์ ๋๊ธ(*Comment*) ํ์ด๋ธ ์ถ๊ฐ
  - **1:N** ๋ฐฉ์์ผ๋ก ์ฐ๊ฒฐ
  - *[./templates/yannjuApp/question_comment.html)](./templates/yannjuApp/question_comment.html)* ์ **๋๊ธ์ถ๊ฐ** ์ธํฐํ์ด์ค ์์ฑ ํ *[./templates/yannjuApp/question_detail.html)](./templates/yannjuApp/question_detail.html)* ์ `include`
    - ์ง๋ฌธ์ ๋ํ ๋๊ธ `์ถ๊ฐ, ์์ , ์ญ์ `์ ๋ํด ๋ชจ๋ ์ ์

    ![์ง๋ฌธ๋๊ธ ์ถ๊ฐ](../img/v3_img(1).PNG)
  - *[./yannjuApp/urls.py](./yannjuApp/urls.py)* ์ `์ถ๊ฐ, ์์ , ์ญ์ ` ๋ชจ๋ mapping
  - *[./yannjuApp/views.py](./yannjuApp/views.py)* ์ `์ถ๊ฐ, ์์ , ์ญ์ ` ๋ชจ๋ ๊ธฐ๋ฅ ์ ์
  - *[./templates/yannjuApp/comment_form.html](./templates/yannjuApp/comment_form.html)* ์ ์ง๋ฌธ์ ๋ํ ๋๊ธ **์์ฑ** form ์์ฑ
  - ๋๊ธ **์ถ๊ฐ**
   
    ![์ง๋ฌธ๋๊ธ ์์ฑ](../img/v3_img(2).PNG)
    ![์ง๋ฌธ๋๊ธ ๊ฒฐ๊ณผ](../img/v3_img(3).PNG)
  - ๋๊ธ **์์ **

    ![์ง๋ฌธ๋๊ธ ์์ ](../img/v3_img(4).PNG)
    ![์ง๋ฌธ๋๊ธ ์์  ๊ฒฐ๊ณผ](../img/v3_img(5).PNG)
  - ๋๊ธ **์ญ์ **
  
    ![์ง๋ฌธ๋๊ธ ์ญ์ ](../img/v3_img(6).png)
    ![์ง๋ฌธ๋๊ธ ์ญ์  ๊ฒฐ๊ณผ](../img/v3_img(7).PNG)
- ### ๋ต๋ณ ๋๊ธ ๊ธฐ๋ฅ ์ถ๊ฐ`(V0.0.3-)`
  - ์ง๋ฌธ์ ๊ดํ ๋๊ธ ๊ธฐ๋ฅ๊ณผ **๋์ผ**ํ๊ฒ ์ ์ฉ
  - *[./templates/yannjuApp/comment_answer.html](./templates/yannjuApp/comment_answer.html)* ์ ๋ต๋ณ์ ๋ํ ๋๊ธ *์ธํฐํ์ด์ค* ์์ฑ
  - *[./yannjuApp/urls.py](./yannjuApp/urls.py)* ์ `์ถ๊ฐ, ์์ , ์ญ์ ` ๋ชจ๋ mapping
  - *[./yannjuApp/views.py](./yannjuApp/views.py)* ์ `์ถ๊ฐ, ์์ , ์ญ์ ` ๋ชจ๋ ๊ธฐ๋ฅ ์ ์
  - *[./templates/yannjuApp/comment_form.html](./templates/yannjuApp/comment_form.html)* ์ Form ๊ฐ์ฒด ์ฌ์ฉ
  - ๊ฒฐ๊ณผ๋ ๋ค์๊ณผ ๊ฐ์
    
    ![๋ต๋ณ๋๊ธ](../img/v3_img(8).PNG) | ![๋ต๋ณ๋๊ธ๊ฒฐ๊ณผ](../img/v3_img(9).PNG) 
    ---| ---|
- ### *[Views.py](./yannjuApp/views.py)* ๋ถ๋ฆฌํ๊ธฐ
  - *[base_views.py](./yannjuApp/views/base_views.py)*, *[answer_views.py](./yannjuApp/views/answer_views.py)*, *[question_views.py](./yannjuApp/views/question_views.py)*, *[comment_views.py](./yannjuApp/views/comment_views.py)* ๋ก view๋ฅผ ๋๋์ด์ค
    - ๊ธฐ์กด `views.py`๋ ์ ์ฒด ์ฃผ์์ผ๋ก ๋จ๊ฒจ๋์์
     
    ![dir ์ฌ์ง](../img/v3_img(10).PNG) 
  - *[./yannjuApp/urls.py](./yannjuApp/urls.py)* ์์๋ ๊ฐ Views ํ์ผ๋ค์ `import` ํ์ฌ ์ ์ฉ
  - *[./config/urls.py](./config/urls.py)* ์ ๊ธฐ์กด `index` ์ธํฐํ์ด์ค View ๋ณ๊ฒฝ
- ### ์ถ์ฒ ๊ธฐ๋ฅ ์ถ๊ฐํ๊ธฐ`(V0.0.3-)`
  - ์ง๋ฌธ ๋ฐ ๋ต๋ณ **์ฌ๋ฌ๊ฐ** ์ ๋ํด **๋ค์** ๊ฐ ๊ด๊ณ๋ฅผ ๋งบ์ ์ ์์ : **๋ค๋๋ค(N:M)๊ด๊ณ**
  - ๊ด๊ณ ์ฌ๋ถ๋ฅผ ๊ฐ ํ์ด๋ธ์ ๋ฃ์ ์ ์๊ธฐ ๋๋ฌธ์ `Question`-`User` ์ฌ์ด์ ๊ด๊ณ๋ฅผ ๋ํ๋ด๋ ํ์ด๋ธ ์ถ๊ฐ
  - `ManyToManyField()` : ๋ค๋๋ค ๊ด๊ณ๋ฅผ ์ํด ์ฌ์ฉ , ์ด๋ `User`๋ชจ๋ธ์ ์ง์  ์์ ์ ํ  ์ ์๊ธฐ ๋๋ฌธ์ `Question`๋ชจ๋ธ์ ์์ฑ
    - ๋ง์ฝ ๋ ๋ชจ๋ธ์ ๋ํ์ฌ ์์ ์ด **๊ฐ๋ฅ** ํ๊ฒฝ์ฐ ๋ ์ค ํ๊ณณ์๋ง ์์ฑํด๋ ์์ฐ์ค๋ฝ๊ฒ *์ฐ๊ฒฐ* ๋จ
  - *[./yannjuApp/models.py](./yannjuApp/models.py)* ์์ `Question`, `Answer`์ **voter** ๋ผ๋ ๋ณ์๋ฅผ ํ ๋นํ๊ณ  `auth` ์ **related_name** ์ถ๊ฐ

    ```python
    # ./yannjuApp/models.py
    #<์๋ต . . . >
    # Create your models here.
    class Question(models.Model):
        # ํ์ค์นผ ํ๊ธฐ๋ฒ์ ์ํ ํด๋์ค ์์ ์ ์ ์๋ค.
        subject = models.CharField('์ ๋ชฉ', max_length=200)
        content = models.TextField('๋ด์ฉ', help_text='๋น๋ฐฉ, ์์ค ๋ฐ ๋๋ฐฐ๊ธ์ ์ญ์ ๋  ์ ์์ต๋๋ค- (/โฝ๏ผผ)')
        create_date =  models.DateTimeField('๋ ์ง')
        auth = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='author_question') #์ ์ํด `question_set`์ด๋ผ๋ ๊ด๊ณ๋งค๋์ ๊ฐ ์๊ฒผ์์
        modify_date = models.DateTimeField(null=True, blank=True)
        
        # User : ์ฐธ์กฐ, `question_set` ์ด๋ผ๋ ๊ด๊ณ๋งค๋์ ๊ฐ ๋ค์ ์๊น, auth์ ์ถฉ๋ / ๋ฐ๋ผ์ related_name ์ ํตํด ํด๊ฒฐ
        voter = models.ManyToManyField(User, related_name='voter_question') 
        
        def __str__(self):
            return self.subject
    #<์๋ต . . . >
    ```
  - `Grid`๋ฅผ ์ด์ฉํ์ฌ **์ถ์ฒ** ์ธํฐํ์ด์ค ์ ์ฉ
    
    ```html
    <!--./yannjuApp/question_detail.html-->
    <!--์๋ต..-->
    <!--์ถ์ฒ ๊ธฐ๋ฅ์ ์ํ grid ์ ์ฉ-->
    <div class = 'row my-3'>
        <div class='col-1'>
            <!--์ถ์ฒ ์์ญ-->
        </div>
        <div class='col-11'>
            <!--์ง๋ฌธ ์์ญ-->
    <!--์๋ต..-->
    </div>
    ```
  - `delete` ๊ธฐ๋ฅ๊ณผ ์ ์ฌํ๊ฒ JS ๋ฅผ ์ด์ฉํ์ฌ ์์ฑ โ ์ถ์ฒ ์ ๋ฌด๋ฅผ *์ง๋ฌธ*
  - *[./yannjuApp/views/vote_views.py](./yannjuApp/views/vote_views.py)* ํ์ผ์ ์์ฑํ ํ ๊ด๋ จ **๊ธฐ๋ฅ** ๊ตฌํ ๋ฐ `url` ๋งคํ
  - ๋ต๋ณ์๋ *๋์ผํ๊ฒ* ์ ์ฉ

  ![์ถ์ฒ๋ฒํผ](../img/v3_img(12).PNG)
   ![์ถ์ฒ๋ฒํผ ํด๋ฆญ](../img/v3_img(13).png) 
   ![์ถ์ฒ ๊ฒฐ๊ณผ](../img/v3_img(14).PNG) 
   - ์์ ์ด ์์ฑํ **์ง๋ฌธ** ์ด๋ **๋ต๋ณ** ์๋ ์ถ์ฒํ  ์ ์์
    
   ![์ถ์ฒ ์ค๋ฅ](../img/v3_img(11)_Err.png)
- ### ์คํฌ๋กค ์ด๊ธฐํ ๋ฌธ์  ํด๊ฒฐ `(V0.0.3-)`
  - ๋ต๋ณ *๋ฑ๋ก, ์์ * ๋ฑ ๊ธฐ๋ฅ ์ํ ํ์ ์คํฌ๋กค์ด ์๋จ์ผ๋ก **์ด๊ธฐํ**
  - `bookmark` ๋ฅผ ์ด์ฉํ์ฌ ๊ธฐ์กด ์คํฌ๋กค ์ ์ง

    ```html
    <!--./templates/yannjuApp/answer_list.html-->
    <!-- ์๋ต . .-->
    {% for answer in question.answer_set.all %}
    <a name="answer_{{answer.id}}"></a> <!--ํ๋ฉด์๋ ์๋ณด์-->  
    <!-- ์๋ต . . -->
    ```
  - *[./yannjuApp/views/comment_views.py](./yannjuApp/views/comment_views.py)* ์ ๋ชจ๋  ํจ์์๋ ๋์ผํ๊ฒ ์ ์ฉ
  - `๋ฑ๋ก, ์ญ์ , ์์ ` ๊ธฐ๋ฅ ์ํ์ **bookmark** ์์น๋ก ์คํฌ๋กค
- ### ์ฌ์ฉ์ ์ ์ ํํฐ ์ฌ์ฉ `(V0.0.4-)`
  - *[./yannjuApp/templatetags/](./yannjuApp/templatetags/)* ํด๋ ์์ฑ
    - `__init__.py` ํ์ผ๊ณผ filter ํ์ผ ์์ฑ
    - *[./yannjuApp/templatetags/yannnju_filter.py](./yannjuApp/templatetags/yannnju_filter.py)* ํ์ผ์ ์์ฑํ์ฌ *์ฌ์ฉ์ ํํฐ ํ์ผ* ์ฌ์ฉ
  - ํ์ํ ํ์ผ ์๋จ์ `{% load yannju_filter %}` <!--markdown ์ฌ์ฉ์ ํํฐ ์ ์--> ์ ํตํด ํํฐ ํ์ผ **๋ถ๋ฌ์ค๊ธฐ**
  - **๋งํฌ๋ค์ด** ์ ์ง๋ฌธ ๋ฐ ๋ต๋ณ ์์ฑ์ *์ฌ์ฉ*
    - *[./templates/yannjuApp/question_detail.html](./templates/yannjuApp/question_detail.html)* ๊ณผ *[./templates/yannjuApp/answer_list.html](./templates/yannjuApp/answer_list.html)* ์ ์๋จ์ `load` ์์ฑ

        ```html
        <!--./templates/yannjuApp/answer_list.html-->
        <!-- ์๋ต . . -->
        <!--<div class = "card-text" style = "white-space : pre-line;"> -->
        <div class = "card-text">
            {{answer.content|mark}}
        </div>
        <!-- ์๋ต . . -->
        ```
      - ๊ธฐ์กด `style='white-space : pre-line'` ๋์  `|mark` ๋ฅผ ํตํด ๋งํฌ๋ค์ด ๊ธฐ๋ฅ ๋ถ๋ฌ์ค๊ธฐ

    ![๋งํฌ๋ค์ด ํ์คํธ](../img/v4_img(1).png)
      - ์์ ๊ฐ์ด ๋งํฌ๋ค์ด(`+, -, *`)์ ์ด์ฉํ ๊ฒ์ด ๋ณด์ฌ์ง
  - ๊ทธ์ธ `simple tag` ๋ฅผ ํตํด ๊ฐ๋จํ๊ฒ *๋ถ๋ฌ์ค๊ธฐ* ๊ฐ๋ฅ **(์ง์  ์ฐพ์๋ณด์)**
- ### Summernote ์ถ๊ฐํ๊ธฐ `(V0.0.4-)`
  - `Summernote`๋ฅผ ์ํด ํ์ํ `css, js, kr` ํ์ผ ๋ค์ด
  - *[static](./static/)*  ํด๋์ ๋ค์ด๋ฐ์ **ํ์ผ** ๋ค ์ฎ๊ฒจ๋์
  - *[base.html](./base.templates/base.html)* ์ `<body>` ๋ถ๋ถ์ `popper` ํ๊ทธ ์ถ๊ฐ

    ```html
    <!--./base.templates/base.html-->
    <!--์๋ต..-->
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.6.3/dist/jquery.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
    <script src = "{% static 'bootstrap.min.js' %}"></script>
    <!--์๋ต..-->
    ```
  - ๊ธฐ์กด์ ๊ฒ์๊ธ์ ์์ฑํ๋ *[./templates/yannjuApp/question_form.html](./templates/yannjuApp/question_form.html)* ์ `Summernote` ๊ด๋ จ ์ฝ๋ ์์ฑ **[16~33 ์ค]**

    ![summernote ์ถ๊ฐ](../img/v4_img(2).png)
- ### ๊ฒ์๊ธฐ๋ฅ ์ถ๊ฐ `(V0.0.4-)`
    - ๊ฒ์์ ์ํด ๊ธฐ์กด `Pagination`์ด ์ด๋ฃจ์ด์ก๋ *[./yannjuApp/views/base_views.py](./yannjuApp/views/base_views.py)* > Index() ๋ถ๋ถ์ `kw` ๋ผ๋ ๋ณ์๋ฅผ ์์ฑ
      - `kw` ๋ผ๋ ๋ณ์๋ฅผ ํตํด `GET` ๋ฉ์๋๋ก ๊ฒ์

        ```python
        #./yannjuApp/views/base_views.py
        #์๋ต . .
        kw = request.GET.get('kw', '') #๊ฒ์ ์ค์ 
        # ์กฐํ
        question_list = Question.objects.order_by('-create_date')
        
        # ๊ฒ์์ด ์ด๋ฃจ์ด์ง๋ค๋ฉด
        if kw:
            question_list = question_list.filter(
                Q(subject__icontains = kw) | #์ ๋ชฉ ๊ฒ์
                Q(content__icontains = kw) | #๋ด์ฉ ๊ฒ์
                Q(auth__username__contains=kw) | #์ง๋ฌธ ๊ธ์ด์ด ๊ฒ์
                Q(answer__auth__username__icontains=kw)  #๋ต๊ธ ๊ฒ์
            ).distinct()
        #์๋ต . .
        ```
      - ์ดํ `context ๋ณ์` ์ `kw`๋ฅผ ์ถ๊ฐํ์ฌ *mapping*
    - *[./templates/yannjuApp/question_list.html](./templates/yannjuApp/question_list.html)* ์ ๊ฒ์์ฐฝ ์ถ๊ฐ
      - ์ด๋ `form` ์ ์ฌ์ฉํ์ง ์์ 
      - ์๋ํ๋ฉด `pagination` ๊ณผ `๊ฒ์` ๋ ๊ฒฝ์ฐ์ ๋ชจ๋ `page` ์ `kw` ๋ฅผ ์ฐธ์กฐํด์ผํ๊ธฐ ๋๋ฌธ
    - **hidden form** ์ ์ด์ฉํ์ฌ `Java Script` ๋ฅผ ํตํด ์ ์ฉ
      - *[./templates/yannjuApp/question_list.html](./templates/yannjuApp/question_list.html)* ํ๋จ์ `form` ํ๊ทธ ์ถ๊ฐ
      - *[./templates/yannjuApp/pagination.html](./templates/yannjuApp/pagination.html)* ์ ๊ฐ ํ์ด์ง ๋ณ `href` ๋ **#** ์ผ๋ก, script ์ฒ๋ฆฌ๋ฅผ ์ํด `data-page` ์์ฑ์ ์ถ๊ฐ
       1. ํ์ด์ง ๋ฒํผ์ ๋๋ฅธ ๊ฒฝ์ฐ โ ๊ฒ์์ด๋ **์ ์ง**/ํ์ด์ง **๋ฒํธ ์ ์ฉ**
       2. ๊ฒ์์ด๋ฅผ ์๋ ฅํ ๊ฒฝ์ฐ โ ๊ฒ์์ด **์ ์ฉ**/ํ์ด์ง ๋ฒํธ **1**
    - *[./templates/yannjuApp/question_list.html](./templates/yannjuApp/question_list.html)* ํ๋จ์ `script` ๋ธ๋ก ์ถ๊ฐ
      - `Script` ๊ธฐ๋ฅ์ ์์ฑ
        1. ํ์ด์ง ๋ฒํผ ํด๋ฆญ
         
        ![ํ์ด์ง๋ค์ด์](../img/v4_img(3).png) 
        2. ๊ฒ์ ๋ฒํผ ํด๋ฆญ
         
        ![๊ฒ์๊ธฐ๋ฅ](../img/v4_img(4).png) 
- ### ๊ฒ์๊ธ ์ ๋ ฌ ๊ธฐ๋ฅ `(V0.0.4-)   `
  - *[./templates/yannjuApp/question_list.html](./templates/yannjuApp/question_list.html)* ์ ๊ฒ์๊ณผ ๊ฐ์ ๋ผ์ธ์ **์ ๋ ฌ๊ธฐ์ค** ๋๋กญ๋ค์ด ์ถ๊ฐ
  - `searchForm` ์ `hidden` ํ์์ผ๋ก ์ ๋ ฌ ์์ฑ์ ์ถ๊ฐ โ **so** ๋ผ๋ ์ด๋ฆ์ผ๋ก id ์ถ๊ฐ
  - `Script` ๋ฅผ ์์ฑ 
    - `select` ํ๊ทธ๊ฐ **change** ๋  ๋๋ง๋ค ๋์
  - *[./yannjuApp/views/base_views.py](./yannjuApp/views/base_views.py)* ์์ `db` ๋ฅผ ์ด์ฉํ์ฌ ์ ๋ ฌ

    ```python
    #./yannjuApp/views/base_views.py
    # ์๋ต. . 
    # ์กฐํ (์ ๋ ฌ)
      # question_list = Question.objects.order_by('-create_date')

      #์ ๋ ฌ ์ฒ๋ฆฌ
      # 1) ์ง๊ณ์ฒ๋ฆฌ, 2) ๋์ ์ผ๋ก ์ถ๊ฐ๋๋ ์์ฑ (ex ์ฐ๋ด๊ณ์ฐ)
      # annotate : ๋์ ์ผ๋ก ์์ฑ ์ ์/ ex. annotate(numvoter = Count('voter')) ์ด๋ฉด, ๊ฐ voter ์นด์ดํธ ํ numvoter ๋ฐํ
      if so == 'recommend':
          question_list = Question.objects.annotate(
              num_voter = Count('voter')).order_by('-num_voter', '-create_date')
      elif so == 'popular':
          question_list = Question.objects.annotate(
              num_answer = Count('answer')).order_by('-num_answer', '-create_date')
      elif so == 'recent':
          question_list = Question.objects.order_by('-create_date')
    # ์๋ต. . 
    ```
    - `annotate` ๋ฅผ ํตํด ๋์  ์์ฑ์ ๋ฐํ
    - ๋์  ์์ฑ์ ์ด์ฉํ์ฌ `์ ๋ ฌ`

  ![์ถ์ฒ์](../img/v4_img(5).png) |![์ธ๊ธฐ์](../img/v4_img(6).png)
  ---|---|
---
## ๐งจ๋ฏธํด๊ฒฐ
โ (0223) `NavBar`๊ฐ ์๋์ผ๋ก ๋ซํ 

~~โ (0224) ๋ก๊ทธ์ธ ์ฐฝ์์ `๋ก๊ทธ์ธ` ๋ฒํผ์ด ๊ธฐ๋ฅ์ ์ํจ~~ **[ํด๊ฒฐ]**