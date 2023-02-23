## 💫Pagenation💫
- ### Pagenation
  - 목록으로 이동할 수 있도록 **인터페이스를** 제공
  - 다른 페이지로 *navigation* 역할
- ### JQuery
  - 여러 인터넷 브라우저 스크립트의 *표준을* 지정
  - HTML의 DOM 조작과 이벤트 제어, 애니메이션 그리고 Ajax까지 웹 화면을 다루는 자바스크립트 라이브러리
- ### 페이지네이션 적용_*(1)*
  - `NavBar`를 이용하여  일정한 크기 미만이 되면 메뉴창을 띄우게 함
  - `Bootstrp`을 적용하기 위해 `static` 디렉토리에 *[./static/bootstrap.min.js](./static/bootstrap.min.js)* 를 넣어둠
  - `NavBar` 속성이 길기 때문에 따로 `templates` 디렉토리에 정의(*[./templates/navbar.html](./templates/navbar.html)*)
  -  [./templates/base.html](./templates/base.html)* 에 `navbar.html`을 **include**
   
        ```html
        <!--./templates/base.html-->
        <body>
            <!--navbar.html을 include 하여 불러옴-->
            {% include 'navbar.html' %}
            <!--공통 템플릿-->
            <!--블럭 내에만 뭐가 들어갈지 신경쓰면 된다-->
            <div class = "container my-3">
        <!--생략-->
        ```
- ### 페이지네이션 적용_*(2)*
  - 게시글 *목록* 인터페이스
  - **테스트** 케이스 *약 300개*를 추가함
   
    ```python
    //./tests.py
    from yannjuApp.models import Question
    from django.utils import timezone

    for i in range(300):
        q = Question(
            subject = f'테스트 데이터 입니다 : [{i:03d}]',
            content = f'테스트 데이터의 내용 입니다 : [{i:03d}]',
            create_date = timezone.now()
        )
        q.save()
    ```
    - 실행시키면 아래와 같이 300개의 테스트 케이스가 만들어짐
     
        ![테스트 케이스](../img/6_img(1).png)
  - `Page` 객체를 이용하여 관리
  - `Pagination` 인터페이스를 만들어서 `Page`를 페이징 할 수 있음
  - *[./templates/pagination.html](./templates/pagination.html)* 에 `Pagination` 인터페이스를 작성
  - *[./yannjuApp/views.py](./yannjuApp/views.py)* 에 페이징 처리를 위해 `context` 를 조정
   
    ```python
    //yannjuApp/views.py
    //생략
    #render가 return 하는게 body의 내용
        # question_list = Question.objects.order_by('-create_date')  #내림차순 = 최신글을 위로
        # context = {'question_list' : question_list} #key 의 명칭은 템플릿에서 사용할 변수 (= 컨텍스트 변수)
        
        # 입력 파라미터
        page = request.GET.get('page', '1') # 페이지
        # 조회
        question_list = Question.objects.order_by('-create_date')
        # 페이징처리
        paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기
        page_obj = paginator.get_page(page)
        context = {'question_list': page_obj}
    //하위생략
    ```
      - 기존과 다르게 `question_list`를 **page** 객체로 줌
  - *[./yannjuApp/views.py](./yannjuApp/views.py)*에서 정의한 `context`를 바탕으로 목록 인터페이스에 기능 부여
  - `add filter`, `paginator.has_next_number`, .. 와 같은 기능을 사용
  - (사진추가~하기~)
- ### 목록의 시작번호 조절
  - 각 페이지(목록페이지) 별 `1` 부터 페이지 번호가 시작
- ### 외부에서 접근하기
  - *[./config/settings.py](./config/settings.py)*에서 `ALLOWED_HOSTS` 에 현재 `IP`를 추가하여 외부에서 접근이 가능하게 함
   
    ```python
    ALLOWED_HOSTS = ['172.30.1.93', '127.0.0.1', 'localhost']
    ```
  - 동일한 `WiFi`를 사용하는 경우 가능