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
  - 게시글 *작성자* 추가하기
    - `Question` 객체에 `User`객체를 **Join**
      - *[./yannjuApp/models.py > Question](./yannjuApp/models.py)* 에 *auth* 추가
       
        ```python
        // ./yannjuApp/models.py
        from django.contrib.auth.models import User
        //(생략 . .)
        auth = models.ForeignKey(User, on_delete=models.CASCADE)
        //(생략 . .)
        ``` 
    - 객체에 *필드*를 추가 한 후 `migration`을 해 주어야함
    - 이때 *필드*가 추가되면서 **테이블 구조**가 바뀐 상태임에도 기존 데이터에도 *적용*을 시켜주어야함
    - 하지만 `author`는 **Not Null** 이므로 default 값이 지정 되어야함
      - `python manage.py makemigrations`를 하게 되면 해당 부분에 대한 **경고** 발생
      - default 값을 정해주고 `python manage.py migrate`를 실행시켜 DB에 적용
      - 다음과 같이 *[./yannjuApp/migrations/0002_question_auth.py](./yannjuApp/migrations/0002_question_auth.py)* 파일이 생성되며 작성됨

        ```python
        //./yannjuApp/migrations/0002_question_auth.py
        //(생략. .)
        operations = [
            migrations.AddField(
                model_name='question',
                name='auth',
                field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
                preserve_default=False,
            ),
        //(생략. .)
        ]
        ```
    - `Answer` 객체에도 동일하게 적용
  - **로그인 계정**만 게시글을 *작성*
- ### 수정 처리
  - 게시글 **작성자** 만 게시글을 수정
  - 오류처리 -> 범용처리
  - *[./templates/yannjuApp/question_form.html](./templates/yannjuApp/question_form.html)*, *[./templates/yannjuApp/answer_form.html](./templates/yannjuApp/answer_form.html)* 과 같이 `form` 작성
  - 이후 각 `Question`, `Answer` 을 불러온 후 `Form` 객체 이용하여 작성
  -  `save()` 를 이용하여 덮어씌우기
- ### 삭제 처리 `(V0.0.2-)`
  - 바로 **삭제** 되는 것을 방지 하기 위해 한번 더 묻는 창을 띄움
  - *[./templates/yannjuApp/question_detail.html](./templates/yannjuApp/question_detail.html)* 에 `삭제` 버튼 추가
    - 이 때 `bt4` 의 버튼 클래스가 아닌 **script** 사용 으로 *동적 처리* 진행
  - `data-uri`: 브라우저는 속성을 모름, 개발자만 알고 정보를 담기만 함 **'data-'** 로 시작하면 사용자 정의 속성 : script 처리를 해야함
  - *[base.html](./templates/base.html)* 에 script block 추가
   
   ```html
  <!--./templates/base.html-->
  <!--생략 . .25-26번줄-->
  <!-- Delete -->
  {% block script %}{% endblock script %}
  <!--생략 . .-->
   ```
  - *[./templates/yannjuApp/question_detail.html](./templates/yannjuApp/question_detail.html)* 에 `<script>` 블록을 만들고 동적처리를 진행

  ```html
  <!--./templates/yannjuApp/question_detail.html-->
  <!--생략..-->
  {% block script %}
  <script>
      $(document).ready(function(){
          $(".delete").on("click", function() {
              if (confirm("정말로 삭제 하시겠습니까?")) {
                  location.href = $(this).data('uri');
              }
          });
      });
  </script>
  {% endblock script %}
  ``` 
  - `script function`을 이용하여 해당 페이지가 준비되고, **delete** 클래스가 **click** 된 경우 `if`문 실행
  - *[./yannjuApp/urls.py](./yannjuApp/urls.py)*에 **delete** 주소를 mapping
  - *[./yannjuApp/views.py](./yannjuApp/views.py)* 에 기능을 작성

    ![삭제img](../img/v2_img(1).PNG)
    ![삭제img](../img/v2_img(2).PNG)
    ![삭제img](../img/v2_img(3).PNG)

- ### 답변 수정 및 삭제하기 `(V0.0.2-)`
  - *질문 수정 및 삭제* 와 **유사하게** 진행
  - *[./templates/yannjuApp/question_detail.html](./templates/yannjuApp/question_detail.html)* 의 답변 부분에 `수정`, `삭제` 버튼 생성
   
    ![답변 수정, 삭제 버튼 생성](../img/v2_img(5).PNG)
  - 각 버튼 당 `url`을 설정하여 mapping
  - *[./yannjuApp/views.py](./yannjuApp/views.py)* 에 기능을 처리하는 함수를 구현
    - 수정 : *[./templates/yannjuApp/answer_form.html](./templates/yannjuApp/answer_form.html)* 을 이용하여 재작성 후 `save`
    - 삭제 : 질문 삭제와 유사하게 `script`를 통해 삭제여부 다시 묻기
- ### Bootstrap Form 이용하기
  - 기존의 `로그인` form 이 아닌 **Bootstrap** 에서 제공하는 Form 을 통해 템플릿 구성
  - *[./config/settings.py](./config/settings.py)* 의 `INSTALLED_APPS` 에 **'bootstrap4'** 을 추가
  - 이후 `bootstrap` form을 사용할 경우 `load` 및 불러오기
   
    ```html
    <!--./templates/yannjuApp/answer_form.html-->
    {% extends 'base.html' %}
    {% load bootstrap4 %}

    {% block content %}
    <form method="POST" class='post-form'>
        {% csrf_token %}
        {% bootstrap_form form %}

        <button type='submit' class="btn btn-primary"> 저장하기 </button>
    </form>
    {% endblock content %}
    ```
    - 상단에 `load`를 통해 **bootstrap** 을 불러온 후 중간에 `{% bootstrap_form form %}` form 사용
    - *[./templates/common/signup.html](./templates/common/signup.html)* 에 기존 작성했던 속성들을 지우고 위처럼 `{% bootstrap_form form %}` form 작성

    ![부트스트랩 폼 사용](../img/v2_img(4).PNG)
  - `로그인, 답변수정` 등에도 동일하게 *적용*
- ### 게시글 댓글기능 추가`(V0.0.2-)`
  - `DB`에 댓글(*Comment*) 테이블 추가
  - **1:N** 방식으로 연결
  - *[./templates/yannjuApp/question_comment.html)](./templates/yannjuApp/question_comment.html)* 에 **댓글추가** 인터페이스 작성 후 *[./templates/yannjuApp/question_detail.html)](./templates/yannjuApp/question_detail.html)* 에 `include`
    - 질문에 대한 댓글 `추가, 수정, 삭제`에 대해 모두 정의

    ![질문댓글 추가](../img/v3_img(1).PNG)
  - *[./yannjuApp/urls.py](./yannjuApp/urls.py)* 에 `추가, 수정, 삭제` 모두 mapping
  - *[./yannjuApp/views.py](./yannjuApp/views.py)* 에 `추가, 수정, 삭제` 모두 기능 정의
  - *[./templates/yannjuApp/comment_form.html](./templates/yannjuApp/comment_form.html)* 에 질문에 대한 댓글 **작성** form 생성
  - 댓글 **추가**
   
    ![질문댓글 작성](../img/v3_img(2).PNG)
    ![질문댓글 결과](../img/v3_img(3).PNG)
  - 댓글 **수정**

    ![질문댓글 수정](../img/v3_img(4).PNG)
    ![질문댓글 수정 결과](../img/v3_img(5).PNG)
  - 댓글 **삭제**
  
    ![질문댓글 삭제](../img/v3_img(6).png)
    ![질문댓글 삭제 결과](../img/v3_img(7).PNG)
- ### 답변 댓글 기능 추가`(V0.0.3-)`
  - 질문에 관한 댓글 기능과 **동일**하게 적용
  - *[./templates/yannjuApp/comment_answer.html](./templates/yannjuApp/comment_answer.html)* 에 답변에 대한 댓글 *인터페이스* 작성
  - *[./yannjuApp/urls.py](./yannjuApp/urls.py)* 에 `추가, 수정, 삭제` 모두 mapping
  - *[./yannjuApp/views.py](./yannjuApp/views.py)* 에 `추가, 수정, 삭제` 모두 기능 정의
  - *[./templates/yannjuApp/comment_form.html](./templates/yannjuApp/comment_form.html)* 의 Form 객체 사용
  - 결과는 다음과 같음
    
    ![답변댓글](../img/v3_img(8).PNG) | ![답변댓글결과](../img/v3_img(9).PNG) 
    ---| ---|
- ### *[Views.py](./yannjuApp/views.py)* 분리하기
  - *[base_views.py](./yannjuApp/views/base_views.py)*, *[answer_views.py](./yannjuApp/views/answer_views.py)*, *[question_views.py](./yannjuApp/views/question_views.py)*, *[comment_views.py](./yannjuApp/views/comment_views.py)* 로 view를 나누어줌
    - 기존 `views.py`는 전체 주석으로 남겨두었음
     
    ![dir 사진](../img/v3_img(10).PNG) 
  - *[./yannjuApp/urls.py](./yannjuApp/urls.py)* 에서도 각 Views 파일들을 `import` 하여 적용
  - *[./config/urls.py](./config/urls.py)* 에 기존 `index` 인터페이스 View 변경
- ### 추천 기능 추가하기`(V0.0.3-)`
  - 질문 및 답변 **여러개** 에 대해 **다수** 가 관계를 맺을 수 있음 : **다대다(N:M)관계**
  - 관계 여부를 각 테이블에 넣을 수 없기 때문에 `Question`-`User` 사이의 관계를 나타내는 테이블 추가
  - `ManyToManyField()` : 다대다 관계를 위해 사용 , 이때 `User`모델은 직접 수정을 할 수 없기 때문에 `Question`모델에 작성
    - 만약 두 모델에 대하여 수정이 **가능** 한경우 둘 중 한곳에만 작성해도 자연스럽게 *연결* 됨
  - *[./yannjuApp/models.py](./yannjuApp/models.py)* 에서 `Question`, `Answer`에 **voter** 라는 변수를 할당하고 `auth` 에 **related_name** 추가

    ```python
    # ./yannjuApp/models.py
    #<생략 . . . >
    # Create your models here.
    class Question(models.Model):
        # 파스칼 표기법에 의한 클래스 임을 알 수 있다.
        subject = models.CharField('제목', max_length=200)
        content = models.TextField('내용', help_text='비방, 욕설 및 도배글은 삭제될 수 있습니다- (/▽＼)')
        create_date =  models.DateTimeField('날짜')
        auth = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='author_question') #에 의해 `question_set`이라는 관계매니저가 생겼었음
        modify_date = models.DateTimeField(null=True, blank=True)
        
        # User : 참조, `question_set` 이라는 관계매니저가 다시 생김, auth와 충돌 / 따라서 related_name 을 통해 해결
        voter = models.ManyToManyField(User, related_name='voter_question') 
        
        def __str__(self):
            return self.subject
    #<생략 . . . >
    ```
  - `Grid`를 이용하여 **추천** 인터페이스 적용
    
    ```html
    <!--./yannjuApp/question_detail.html-->
    <!--생략..-->
    <!--추천 기능을 위한 grid 적용-->
    <div class = 'row my-3'>
        <div class='col-1'>
            <!--추천 영역-->
        </div>
        <div class='col-11'>
            <!--질문 영역-->
    <!--생략..-->
    </div>
    ```
  - `delete` 기능과 유사하게 JS 를 이용하여 작성 → 추천 유무를 *질문*
  - *[./yannjuApp/views/vote_views.py](./yannjuApp/views/vote_views.py)* 파일을 생성한 후 관련 **기능** 구현 및 `url` 매핑
  - 답변에도 *동일하게* 적용

  ![추천버튼](../img/v3_img(12).PNG)
   ![추천버튼 클릭](../img/v3_img(13).png) 
   ![추천 결과](../img/v3_img(14).PNG) 
   - 자신이 작성한 **질문** 이나 **답변** 에는 추천할 수 없음
    
   ![추천 오류](../img/v3_img(11)_Err.png)
- ### 스크롤 초기화 문제 해결 `(V0.0.3-)`
  - 답변 *등록, 수정* 등 기능 수행 후에 스크롤이 상단으로 **초기화**
  - `bookmark` 를 이용하여 기존 스크롤 유지

    ```html
    <!--./templates/yannjuApp/answer_list.html-->
    <!-- 생략 . .-->
    {% for answer in question.answer_set.all %}
    <a name="answer_{{answer.id}}"></a> <!--화면에는 안보임-->  
    <!-- 생략 . . -->
    ```
  - *[./yannjuApp/views/comment_views.py](./yannjuApp/views/comment_views.py)* 의 모든 함수에도 동일하게 적용
  - `등록, 삭제, 수정` 기능 수행시 **bookmark** 위치로 스크롤
- ### 사용자 정의 필터 사용 `(V0.0.4-)`
  - *[./yannjuApp/templatetags/](./yannjuApp/templatetags/)* 폴더 생성
    - `__init__.py` 파일과 filter 파일 생성
    - *[./yannjuApp/templatetags/yannnju_filter.py](./yannjuApp/templatetags/yannnju_filter.py)* 파일을 생성하여 *사용자 필터 파일* 사용
  - 필요한 파일 상단에 `{% load yannju_filter %}` <!--markdown 사용자 필터 정의--> 을 통해 필터 파일 **불러오기**
  - **마크다운** 을 질문 및 답변 작성시 *사용*
    - *[./templates/yannjuApp/question_detail.html](./templates/yannjuApp/question_detail.html)* 과 *[./templates/yannjuApp/answer_list.html](./templates/yannjuApp/answer_list.html)* 의 상단에 `load` 작성

        ```html
        <!--./templates/yannjuApp/answer_list.html-->
        <!-- 생략 . . -->
        <!--<div class = "card-text" style = "white-space : pre-line;"> -->
        <div class = "card-text">
            {{answer.content|mark}}
        </div>
        <!-- 생략 . . -->
        ```
      - 기존 `style='white-space : pre-line'` 대신 `|mark` 를 통해 마크다운 기능 불러오기
    - 그외 `simple tag` 를 통해 간단하게 *불러오기* 가능 **(직접 찾아보자)**

---
## 🧨미해결
→ (0223) `NavBar`가 자동으로 닫힘 

~~→ (0224) 로그인 창에서 `로그인` 버튼이 기능을 안함~~ **[해결]**