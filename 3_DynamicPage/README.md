## π«DynamicPageπ«
 - ### `View` ν¨μλ₯Ό μ΄μ©ν μ§λ¬Έ μμΈ κΈ°λ₯ κ΅¬ν
   - μμνμΌ νμ : ννλ¦Ώ νμΌκ³Ό λ³μλͺ©λ‘μ μ΄μ©νμ¬ `render()` νΈμΆ β *[views.py](./yannjuApp/views.py)*
   - `render()`λ html νμΌμ μ°κ²°
   - `template` μμ±
     1. [templates](./templates/) ν΄λ μμ±
     2. *[settings.py](./config/settings.py)*  μ TEMPLATES > DIR > `[BASE_DIR/templates]` ν΄λ λ±λ‘
      - νμ¬ *[settings.py](./config/settings.py)*  > TEMPLATES > `'APP_DIRS': True`, μ΄λ―λ‘ App λ°μ *templates* ν΄λκ° μλ **μ€λ₯κ° λμ§ μμ**!
    - templates > *[question_list.html](../3_DynamicPage/templates/yannjuApp/question_list.html)* λ₯Ό μ΄μ©νμ¬ μΉ νλ©΄μ λμΈ μ μμ
 
      ![htmlImg](../img/3_img(1).png)
  - ### template λ§λ€κΈ°
    - `{%(λͺλ Ήμ΄)%}` λ°©μμΌλ‘ ννλ¦Ώμ μμ± (ν΄λΉ μμμ μλ²μμ μ²λ¦¬)
     
      ``` html
        <!--./templates/yannjuApp/question_index.html-->
      {% if question_list %}
      <ul>
        {% for question in question_list %}
            <li><a href = 'yannjuApp/{{question.id}}'>{{question.subject}}</a></li>
        {% endfor %}
          </ul>
        {% else %}
          <p>μ§λ¬Έμ΄ μμ΅λλ€ . . γ γ γ</p>
        {% endif %}
      ```
    - μμ κ°μ΄ μμ±λ htmlμ μλμ κ°μ κ²°κ³Όλ¬Ό λμΆ
   
      ![templateImg](../img/3_img(2).png)
   - ### URL mapping μΆκ° : κ°μ Έμ¨ Question λͺ©λ‘μ *Contents*λ€μ mapping
     - `path('<int:question_id>/', views.detail)` μ κ°μ΄ μ μνμ¬ *[urls.py](./yannjuApp/urls.py)* μ μΆκ° (*λΌμ°ν λ³μ*)
     - `<int : question_id>` λ‘ μμ±νμ¬ λ¬Έμμ΄μ `int`νμΌλ‘ λ³ννμ¬ μ¬μ©
     - *[views.py](./yannjuApp/views.py)* μ `detail ` ν¨μ μ μ
       - λ§€κ°λ³μμ *λΌμ°νλ³μ* μ΄λ¦μ κΌ­ **λμΌ**νκ² ν΄μΌν¨
     - *[templates/yannjuApp/question_detail.html](./templates/yannjuApp/question_detail.html)* ννλ¦Ώμ μμ±νμ¬ contents **μΆλ ₯**

        ``` html
        <!--./templates/yannjuApp/question_detail.html-->
        <h1>μ λͺ© : {{question.subject}} ~(>_<γ)οΌΌ</h1>
        <div>
            λ΄μ© : 
        </div>
        <div>
            {{question.content}}  β‘(βοΉβ)β‘
        </div>
        ``` 
     - μμκ°μ΄ μμ±νλ©΄ μλμ κ°μ κ²°κ³Ό λμΆ
      
        ![detailImg](../img/3_img(3).png)
  - ### **404 Error** λ°μμν€κΈ°
    - *[views.py](./yannjuApp/views.py)* μμ `get_object_or_404` λ₯Ό import
     
      ``` python
      get_object_or_404(Question, pk=question_id)
      ```
    - μμ κ°μ΄ μμ±ν  κ²½μ° μλͺ»λ νμ΄μ§μ μ κ·Ό μ **μ€λ₯** νμ΄μ§λ₯Ό λ³΄μ¬μ€
     
       ![404Img](../img/3_img(4).png)
  - ### URL **λ³μΉ­**μ μ€μ  : μ¬μ΄νΈ κ°νΈμ΄ λ§μ κ²½μ° ν¨μ¬ μ μ©νκ² μμ©
    - *[yannjuApp/urls.py](./yannjuApp/urls.py)* μμ `name`μ΄λΌλ μμ±μ μΆκ°
    - `name` μ ν λΉλ λ³μΉ­μΌλ‘ λ§ν¬λ₯Ό κ°μ Έμ΄
     
      ``` html
      <!--./templates/yannjuApp/question_detail.html-->
      {% comment %} <li><a href = '{{question.id}}'>{{question.subject}}</a></li> {% endcomment %}
      <li><a href = "{% url 'detail' question.id %}">{{question.subject}}</a></li>
      ```
    - *[config/urls.py](./config/urls.py)* μμ **urlμ λ³κ²½**νμ¬λ λ€λ₯Έ λΆλΆμμλ μ κ²½μ°μ§ μμλ λ¨ β μ μ°ν μμ±μ΄ κ°λ₯
     
      ![urlλ³μΉ­](../img/3_img(5).png)
  -  ### **λ€μμ€νμ΄μ€** μ€μ 
     -  μ±μ΄ λ§μ κ²½μ° λ³μΉ­ μΆ©λ κ°λ₯μ±
     -  *[yannjuApp/urls.py](yannjuApp/urls.py)* μμ `app_name` λ³μμ λ€μμ€νμ΄μ€ ν λΉ
     -  *[question_detail.html](templates/yannjuApp/question_detail.html)* μμ ν΄λΉ λ€μμ€νμ΄μ€λ₯Ό μλμκ°μ΄ μ¬μ©
       
        ``` html
        <!--./templates/yannjuApp/question_detail.html-->
        {% comment %} <a href = "{% url 'index' %}">λͺ©λ‘λ³΄κΈ°</a> {% endcomment %}
        <a href = "{% url 'yannjuName:index' %}">λͺ©λ‘λ³΄κΈ°</a> <!--λ€μμ€νμ΄μ€ μ€μ -->
        ```
   - ### **Form** μ ν΅ν΄ μλ ₯λ°κΈ°
     - *Modelκ³Ό* μλΉν μ μ¬
     - **POST** λ₯Ό μ΄μ©νμ¬ data λ₯Ό μ¨κΈ°κ³ , κΈΈμ΄μ μ νμ΄ μλλ‘ νμ© : methodμ default λ `get`
     - **CSRF**(Cross Site Request Forgery)
       - django μμ formμ λ°μμ *μΈμ *
       - form μ΄ μμ΄ λ³μ‘° μν¬ μ μκΈ° λλ¬Έμ μμ²­μ κ΅¬λΆ
       - μ λ³΄κ° λ€μ΄μ€λλ° *λμκ°* ν¨κ» λ€μ΄μ€λκ°, νμΈ
        
          ![csrf](../img/3_img(6).png)
        - *hidden type*μΌλ‘ μλ ₯λμ΄ λμκ° ν¨κ» valueλ‘ λ€μ΄μ΄ 
  - ### λ΅λ³ λ±λ‘ URL Mapping β *Form* κ°μ²΄μμ μ λ³΄ **μ»μ΄μ€κΈ°**
    -  get : `?csrftoken..=XXX&name=μλ ₯κ° . . ` κ³Ό κ°μ΄ urlμ λ΄κΉ
    -  `print(request.GET)` κ°μ λͺλ Ήμ΄λ₯Ό μ¬μ©νμ¬ λ΄μ©μ νμΈν  μ μμ 
    -  `answer_set` : κ΄κ³ λ§€λμ  (**λͺ¨λΈλͺ_set** μΌλ‘ μ¬μ©)
       -  λκ΅°κ°κ° Foreign Keyλ₯Ό λ§λ€λ©΄ μλμΌλ‘ λ§λ€μ΄μ£Όκ³  κ·Έμ κ΄λ ¨λ *answerμ λν μΌμ λμμ€*
       -  shellμ ν  λ `question = q`μ κ°μ΄, *FKλ₯Ό* μ ν΄μ£Όμ§ μμλ λλ€.
    -  `create` : *μμ± & μ μ₯*μ νλ²μ ν΄μ€
    
        ![λ΅λ³λ±λ‘](../img/3_img(7).png)  |![DB](../img/3_img(8).png)
        --- | --- | 
  - ### λ΅λ³ λ±λ‘ λͺ©λ‘μ **νλ©΄μ νμ**
   
      ``` html
      <!--./templates/yannjuApp/question_detail.html-->
      <h5>{{question.answer_set.count}}κ°μ λ΅λ³μ΄ μμ΅λλ€.</h5>
      <div>
          <ul>
              {% for answer in question.answer_set.all %}
                  <li>{{answer.content}}</li>
              {% endfor %}
          </ul>
      </div>
      ``` 
    - `answer_set.count` λ₯Ό ν΅ν΄ νμ¬ `question`κ³Ό κ΄λ ¨λ `answer`λ€μ μλ₯Ό count
    - `answer_set.all` μ ν΅ν΄ νμ¬ `question`κ³Ό κ΄λ ¨λ λͺ¨λ  `answer` λ₯Ό κ°μ Έμ΄
     
      ![λ΅λ³λͺ©λ‘](../img/3_img(9).png)