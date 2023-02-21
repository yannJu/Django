## 💫StyleSheet💫
- ### *정적 파일* 처리
  - *[config/settings](./config/settings.py)* 에서 `STATICFILES_DIRS - [
    BASE_DIR / 'static',
]` 을 작성 → 이때 BASE_DIR 하위로 지정
  - 여러개를 지정할 수 있다.
  - 프로젝트 **root**에 `static`폴더 생성 : django를 거치지 않고 바로 폴더에 접근함
- ### 웹페이지에 **StyleSheet** 적용
  - `static`하위에 *[static/style.css](./static/style.css)* 을 생성하여 StyleSheet 작성