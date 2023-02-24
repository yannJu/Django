## 🎆Final Application🎆
### `yannJu`
---
- ### 회원관리 앱 추가
  - `django-admin startapp` 명령어를 이용하여 **common** 이라는 app을 추가
  - *[./config/settings.py > INSTALLED_APPS](./config/settings.py)* 에 `App` 접근을 위해 `common` 을 추가
  - `auth`를 이용하는데 주로 `CBV ` 즉 **클래스** 기준으로 관리
- ### 로그인 유저 동적으로 관리
  - **Login**
    - *[templates/navbar.html](templates/navbar.html)* 에 *로그인 주소*로 이동할 수 있도록 수정
    - *로그인주소* 는 위에서 새로 추가한 `common` 앱에서 관리
    - *[./common/urls.py](./common/urls.py)*  에서 `로그인 주소` URL을 추가
     
        ```python
        //./common/urls.py
        //<상위생략>
        path('login', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
        //<하위생략>
        ```
    - `LoginView`를 이용하여 *Login 관리* 를 보다 편하게 이용할 수 있음
    - 로그인 URL로 이동하기 위해 `template_name`을 할당
    - 이후 **로그인 템플릿** 제작 (*[./templates/common/login.html](./templates/common/login.html)*) 및 에러처리
    - 에러처리는 `{% include "form_errors.html" %}` 를 추가하여 *[./templates/form_errors.html](./templates/form_errors.html)* 에서 로그인 에러를 처리
     
    ![오류1](../img/img1.png)|![오류2](../img/img2.png)
    --- | --- | 
  - **Logout**
    - *[templates/navbar.html](templates/navbar.html)* 에 로그인과 동일하게 추가
    - 단 **로그인 상태**를 확인해야함
     
        ```html
        <!--templates/navbar.html--d>
        {% if user.is_authenticated %}
                <li class="nav-item ">
                    <a class="nav-link" href = '#'> {{user.username}} 님 ฅʕ•̫͡•ʔฅ 반갑습니다 !</a>                   
                </li>
                <li class="nav-item ">
                    <a  class="nav-link" href="{% url 'common:logout' %}">
                        <i class="fa-solid fa-right-to-bracket"></i>
                        로그아웃
                    </a>                   
                </li>
            {% else %}
                <li class="nav-item ">
                    <a  class="nav-link" href="{% url 'common:login' %}">로그인하기 .______.</a>                   
                </li>
            {% endif %}
        ``` 
        - `is_authenticated` 를 이용하여 `true`라면 로그인 상태이므로 **로그아웃 버튼**을 띄워준다.
        - `false` 인 경우 로그아웃 상태 이므로 **로그인 버튼** 을 띄워준다.
         
        ![](../img/img3.PNG)
        ![](../img/img4.PNG)
      - 로그아웃에 성공하게 되면 **초기화면으로** 돌아가도록 한다.
- ### 유저이미지 랜덤하게 제공 [(randomuser.me)](http://www.randomuser.me) 가능
- ### 회원가입 기능 추가
  - *유효성 검사* 및 Primary Key 를 체크 *(중복검사)* 해야함
  - `django.contrib.auth ` 에서 **회원관리** 기능을 제공
  - *[./templates/common/login.html](./templates/common/login.html)* 의 Login 헤더 옆에 `회원가입` 버튼을 생성 → **Grid** 를 부트스트랩을 이용하여 적용

    ![회원가입 버튼 생성](../img/img_%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%20%EB%B2%84%ED%8A%BC.PNG)
  - *[./common/urls.py](./common/urls.py)*에 다음과 같이 `signup` URL을 *mapping*
   
    ```python
    //./common/urls.py
    //(... 생략 ...)
    from . import views
    //(... 생략 ...)
    urlpatterns = [
    //(... 생략 ...)
    path('signup/', views.signup, name='signup'),
        ]
    ```
  - **Form** 만들기
    - *[./common/forms.py](./common/forms.py)* 파일에 `UserForm`이라는 form을 생성
     
        ```python
        //./common/forms.py
        from django import forms
        from django.contrib.auth.forms import UserCreationForm
        from django.contrib.auth.models import User

        class UserForm(UserCreationForm):
            email = forms.EmailField(label='이메일')
            
            class Meta:
                model = User
                fields = ('username', 'email')
        ``` 
        - email과 같이 **재정의**할 수 있음
  - Signup **Template** 만들기
    - *[./templates/common/signup.html](./templates/common/signup.html)* 에 사용자이름, 비밀번호, 이메일 입력을 받을 수 있도록 *Template* 생성
    - `as_p`로 묶어 작성할 수 있지만, 보다 가시성을 높이기 위해 `field` 각각 작성

    ![회원가입창](../img/img_%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%20%ED%8E%98%EC%9D%B4%EC%A7%80.PNG)
  - `AUTH_PASSWORD_VALIDATORS` 로 인해 보다 *복잡하게* Passwd를 관리할 수 있음
  - *[./common/views.py](./common/views.py)*
   
    ```python
    //./common/views.py
    //(생략..)
    if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
    //(생략..)
    ```
    - `authenticate` : user 이름을 체킹하고있다면 비밀번호 일치를 확인
      - user name : **O**, pwd : **O** → user객체 **생성**
      - user name : **X** 이거나 pwd : **X**  → **None** 을반환
    - `login` 을 거친 후 회원 *생성*
- ### 회원가입 에러 처리
  - **Login/Logout**  과 동일하게 *[form_errors.html](./templates/form_errors.html)* 을 연동시킴

    ![](../img/img_errTest.png) 
- ### 회원가입 및 로그인 테스트
  - 회원가입 창에서 *정보* 입력   
   
    ![회원가입](../img/img_%EB%A1%9C%EA%B7%B8%EC%9D%B8%EA%B3%BC%EC%A0%95.PNG) |![회원가입 후 로그인](../img/img_%EB%A1%9C%EA%B7%B8%EC%9D%B8%EC%84%B1%EA%B3%B51.PNG)
    ---|---|
  - 로그인 창에서 *로그인* 

    ![로그인](../img/img_%EB%A1%9C%EA%B7%B8%EC%9D%B8.PNG)|![로그인후 결과](../img/img_%EB%A1%9C%EA%B7%B8%EC%9D%B8%EC%84%B1%EA%B3%B52.PNG)
    ---|---|
- ### 로그인 버튼 위치 변경
  - 로그인 헤더와 같은 라인에 있던 위치를  변경
  - 로그인 **버튼** 아래에 회원가입 버튼 *추가*

  ![로그인 버튼 위치 변경](../img/img_%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85ver2.PNG) 
- ### 게시글 각각에 허용 범위 설정
  - **로그인 계정**만 게시글을 *작성*
  - **게시글 작성자**만 *수정 및 삭제* 가능
  - 모든 게시글은 **전체보기**
---
## 🧨미해결
→ (02230) `NavBar`가 자동으로 닫힘 