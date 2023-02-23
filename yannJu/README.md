## 🎆Final Application🎆
### `yannJu`
---
- ### 회원관리 앱 추가
  - `django-admin startapp` 명령어를 이용하여 **common** 이라는 app을 추가
  - *[./config/settings.py > INSTALLED_APPS](./config/settings.py)* 에 `App` 접근을 위해 `common` 을 추가
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
- 유저이미지 랜덤하게 제공 [(randomuser.me)](http://www.randomuser.me) 가능
---
## 🧨미해결
→ `NavBar`가 자동으로 닫힘