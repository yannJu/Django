### 💫DynamicPage💫
 - `View` 함수를 이용한 질문 상세 기능 구현
   - 서식파일 필요 : 템플릿 파일과 변수목록을 이용하여 `render()` 호출 → *[views.py](./yannjuApp/views.py)*
   - `render()`는 html 파일을 연결
   - `template` 생성
     1. [templates](./templates/) 폴더 생성
     2. *[settings.py](./config/settings.py)*  의 TEMPLATES > DIR > `[BASE_DIR/templates]` 폴더 등록
      - 현재 *[settings.py](./config/settings.py)*  > TEMPLATES > `'APP_DIRS': True`, 이므로 App 밑에 *templates* 폴더가 와도 **오류가 나지 않음**!
    - templates > *[question_list.html](../3_DynamicPage/templates/yannjuApp/question_list.html)* 를 이용하여 웹 화면을 띄울 수 있음
 
    ![htmlImg](../img/3_img(1).png)
    - 