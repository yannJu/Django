## 💫StyleSheet💫
- ### *정적 파일* 처리
  - *[config/settings](./config/settings.py)* 에서 `STATICFILES_DIRS - [
    BASE_DIR / 'static',
]` 을 작성 → 이때 BASE_DIR 하위로 지정
  - 여러개를 지정할 수 있다.
  - 프로젝트 **root**에 `static`폴더 생성 : django를 거치지 않고 바로 폴더에 접근함
- ### 웹페이지에 StyleSheet 적용
  - `static`하위에 *[static/style.css](./static/style.css)* 을 생성하여 *StyleSheet* 작성
  - *[tmplates/yannjuApp/question_detail.html](./tmplates/yannjuApp/question_detail.html)* 에서 외부 css 파일을 `link`를 이용하여 불러옴

    ```html
    <!--tmplates/yannjuApp/question_detail.html-->
    {% load static %} <!--static lib을 사용함을 의미-->
    <link rel = "stylesheet" type = "text/css" href = "{% static 'style.css' %}">
    ```
  - `{% load static %}` 을 호출하여 이후 예상치 못하게 `static`의 경로가 바뀌는 경우를 대비
    - 따라서 `href`에 마치 *URL별칭*을 달듯 `static` 만을 사용하여 해결