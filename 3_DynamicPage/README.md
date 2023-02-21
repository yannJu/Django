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
        <!--./templates/yannjuApp/question_index.html-->
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
        <!--./templates/yannjuApp/question_detail.html-->
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
  - **404 Error** 발생시키기
    - *[views.py](./yannjuApp/views.py)* 에서 `get_object_or_404` 를 import
     
      ``` python
      get_object_or_404(Question, pk=question_id)
      ```
    - 위와 같이 작성할 경우 잘못된 페이지에 접근 시 **오류** 페이지를 보여줌
     
       ![404Img](../img/3_img(4).png)
  - URL **별칭**을 설정 : 사이트 개편이 많은 경우 훨씬 유용하게 작용
    - *[yannjuApp/urls.py](./yannjuApp/urls.py)* 에서 `name`이라는 속성을 추가
    - `name` 에 할당된 별칭으로 링크를 가져옴
     
      ``` html
      <!--./templates/yannjuApp/question_detail.html-->
      {% comment %} <li><a href = '{{question.id}}'>{{question.subject}}</a></li> {% endcomment %}
      <li><a href = "{% url 'detail' question.id %}">{{question.subject}}</a></li>
      ```
    - *[config/urls.py](./config/urls.py)* 에서 **url을 변경**하여도 다른 부분에서는 신경쓰지 않아도 됨 → 유연한 작성이 가능
     
      ![url별칭](../img/3_img(5).png)
  -  **네임스페이스** 설정
     -  앱이 많은 경우 별칭 충돌 가능성
     -  *[yannjuApp/urls.py](yannjuApp/urls.py)* 에서 `app_name` 변수에 네임스페이스 할당
     -  *[question_detail.html](templates/yannjuApp/question_detail.html)* 에서 해당 네임스페이스를 아래와같이 사용
       
        ``` html
        <!--./templates/yannjuApp/question_detail.html-->
        {% comment %} <a href = "{% url 'index' %}">목록보기</a> {% endcomment %}
        <a href = "{% url 'yannjuName:index' %}">목록보기</a> <!--네임스페이스 설정-->
        ```
   - **Form** 을 통해 입력받기
     - *Model과* 상당히 유사
     - **POST** 를 이용하여 data 를 숨기고, 길이에 제한이 없도록 활용 : method의 default 는 `get`
     - **CSRF**(Cross Site Request Forgery)
       - django 에서 form을 받음을 *인정*
       - form 이 없이 변조 시킬 수 있기 때문에 요청을 구분
       - 정보가 들어오는데 *난수가* 함께 들어오는가, 확인
        
          ![csrf](../img/3_img(6).png)
        - *hidden type*으로 입력되어 난수가 함께 value로 들어옴 
  - 답변 등록 URL Mapping → *Form* 객체에서 정보 **얻어오기**
    -  get : `?csrftoken..=XXX&name=입력값 . . ` 과 같이 url에 담김
    -  `print(request.GET)` 같은 명령어를 사용하여 내용을 확인할 수 있음 
    -  `answer_set` : 관계 매니저 (**모델명_set** 으로 사용)
       -  누군가가 Foreign Key를 만들면 자동으로 만들어주고 그와 관련된 *answer에 대한 일을 도와줌*
       -  shell을 할 때 `question = q`와 같이, *FK를* 전해주지 않아도 된다.
    -  `create` : *생성 & 저장*을 한번에 해줌
    
        ![답변등록](../img/3_img(7).png)  |![DB](../img/3_img(8).png)
        --- | --- | 
  - 답변 등록 목록을 **화면에 표시**
   
      ``` html
      <!--./templates/yannjuApp/question_detail.html-->
      <h5>{{question.answer_set.count}}개의 답변이 있습니다.</h5>
      <div>
          <ul>
              {% for answer in question.answer_set.all %}
                  <li>{{answer.content}}</li>
              {% endfor %}
          </ul>
      </div>
      ``` 
    - `answer_set.count` 를 통해 현재 `question`과 관련된 `answer`들의 수를 count
    - `answer_set.all` 을 통해 현재 `question`과 관련된 모든 `answer` 를 가져옴
     
      ![답변목록](../img/3_img(9).png)