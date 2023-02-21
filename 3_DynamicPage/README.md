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
  - template 만들기
    - `{%(명령어)%}` 방식으로 템플릿을 작성 (해당 양식은 서버에서 처리)
     
      ``` html
      {% if question_list %}
      <ul>
        {% for question in question_list %}
            <li><a href = 'yannjuApp/{{question.id}}'>{{question.subject}}</a></li>
        {% endfor %}
          </ul>
        {% else %}
          <p>질문이 없습니다 . . ㅎ ㅅ ㅎ</p>
        {% endif %}
      ```
    - 위와 같이 작성된 html은 아래와 같은 결과물 도출
   
      ![templateImg](../img/3_img(2).png)
   - URL mapping 추가 : 가져온 Question 목록의 *Contents*들을 mapping
     - `path('<int:question_id>/', views.detail)` 와 같이 정의하여 *[urls.py](./yannjuApp/urls.py)* 에 추가 (*라우팅 변수*)
     - `<int : question_id>` 로 작성하여 문자열을 `int`형으로 변환하여 사용
     - *[views.py](./yannjuApp/views.py)* 에 `detail ` 함수 정의
       - 매개변수에 *라우팅변수* 이름을 꼭 **동일**하게 해야함
     - *[templates/yannjuApp/question_detail.html](./templates/yannjuApp/question_detail.html)* 템플릿을 생성하여 contents **출력**

        ``` html
        <h1>제목 : {{question.subject}} ~(>_<。)＼</h1>
        <div>
            내용 : 
        </div>
        <div>
            {{question.content}}  ≡(▔﹏▔)≡
        </div>
        ``` 
     - 위와같이 작성하면 아래와 같은 결과 도출
      
        ![detailImg](../img/3_img(3).png)