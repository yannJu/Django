## 💫StyleSheet💫
- ### *정적 파일* 처리
  - *[config/settings](./config/settings.py)* 에서 `STATICFILES_DIRS - [
    BASE_DIR / 'static',
]` 을 작성 → 이때 BASE_DIR 하위로 지정
  - 여러개를 지정할 수 있다.
  - 프로젝트 **root**에 `static`폴더 생성 : django를 거치지 않고 바로 폴더에 접근함
- ### 웹페이지에 `StyleSheet` 적용
  - `static`하위에 *[static/style.css](./static/style.css)* 을 생성하여 *StyleSheet* 작성
  - *[tmplates/yannjuApp/question_detail.html](./tmplates/yannjuApp/question_detail.html)* 에서 외부 css 파일을 `link`를 이용하여 불러옴

    ```html
    <!--tmplates/yannjuApp/question_detail.html-->
    {% load static %} <!--static lib을 사용함을 의미-->
    <link rel = "stylesheet" type = "text/css" href = "{% static 'style.css' %}">
    ```
  - `{% load static %}` 을 호출하여 이후 예상치 못하게 `static`의 경로가 바뀌는 경우를 대비
    - 따라서 `href`에 마치 *URL별칭*을 달듯 `static` 만을 사용하여 해결
- ### `BootStrap` 을 이용하기
  - 원하는 css 파일을 사용(*[./static/bootstrap.min.css](./static/bootstrap.min.css)*)
    ```html
    <!--tmplates/yannjuApp/question_list.html-->
    {% load static %} <!--static lib을 사용함을 의미-->
    <link rel = "stylesheet" type = "text/css" href = "{% static 'bootstrap.min.css' %}">
    ``` 
    - `href`를 ` bootstrap.min.css`로 작성
  - 태그를 통하여 style sheet 적용(*[./templates/yannjuApp/question_list.html](./templates/yannjuApp/question_list.html)*)
   
    ```html
    <!--tmplates/yannjuApp/question_list.html-->
    <div class = "container my-3">
            <table class = 'table table-hover'>
                <thead>
                    <tr class = "thead-dark">
                        <th>번호</th>
                        <th>제목</th>
                        <th>작성일시</th>
                    </tr>
                </thead>
            <!-- ( 생략 ) -->
        </table>
    </div>
    ```
    - `my -3` : **m**argin **y**좌표 **3**만큼 
    - `container` : container처럼 묶고 가운데에 띄워줌
    - `table-hover` : **마우스를** 목록에 대면 컬러 **이벤트** 동작
    - `thead-dark` : thead 를 **dark** 컬러로 변경
     
    ![bootstrapImg](../img/4_img(1).png) 
  - 하위 목록 또한 **테이블로** 구성, *폭 너비 넓어짐*
  - 그 외에도 `flex`, `badge`, `white-space`, `card`, . . 등이 있음
- ### MTV (Model Template View)
  - 관심사를 *분리*하여 **복잡도**를 *낮추고* 관리 및 유지보수가 가능해짐
  - `Model` : 데이터 처리
  - `Template` : 표현 (presentation - html)
  - `View` : 데이터 가공
-  ### 코드 중복 해결
   -  *[./static/bootstrap.min.css](./static/bootstrap.min.css)* 파일을 *[templates](./templates/)* 하위 파일들에서 사용하게 되는데 만약 그 하위 파일이 *매우 많은 경우* **코드 중복** 발생
   -  따라서 **HTML**과 **템플릿 상속** 을 통해 해결
      -  *[./templates/base.html](./templates/base.html)* 에 HTML 문서 작성
      -  `bootstrap.min.css`의 위치를 `base.html`에 작성하여 코드 중복 해결
      -  `body`내에 `block`문만 신경쓰면 된다.
      -  이후 다른 StyleSheet templates Html 들 상단에 extends 작성, block 문 내부로 이동시킴
          ```html
          <!--./templates/yannjuApp/question_list.html-->
          {% extends 'base.html' %}

          <div class = "container my-3">
            {% block content %}
            <!--생략-->
            {% endblock content %}
          </div>
          ```
        - 또한 *[./templates/yannjuApp/question_detail.html](./templates/yannjuApp/question_detail.html)*  와 *[./templates/yannjuApp/question_list.html](./templates/yannjuApp/question_list.html)*  와  모두 전체적으로 `<div container>` 로 감싸져 있으므로 **공통 block**  으로 빼내어 사용
          ```html
          <!--templates/base.html-->
          <div class = "container my-3">
              {% block content %}{% endblock content %}
          </div>
          ``` 
 - ### `CDN`을 이용하여 아이콘 사용
   - `font awesome cdn`을 통해 **아이콘을** 사용
   - 아이콘 **폰트** 이기 때문에 *글자처럼* 사용 가능
   - *[./templates/base.html](./templates/base.html)* 에 `font awesome cdn` 태그를 추가
   - `font awesome`에서 원하는 아이콘을 선택하여 태그 추가
   ![이미지 업로드](../img/4_img(2).png) 