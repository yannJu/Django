## ๐ซPagenation๐ซ
- ### Pagenation
  - ๋ชฉ๋ก์ผ๋ก ์ด๋ํ  ์ ์๋๋ก **์ธํฐํ์ด์ค๋ฅผ** ์ ๊ณต
  - ๋ค๋ฅธ ํ์ด์ง๋ก *navigation* ์ญํ 
- ### JQuery
  - ์ฌ๋ฌ ์ธํฐ๋ท ๋ธ๋ผ์ฐ์  ์คํฌ๋ฆฝํธ์ *ํ์ค์* ์ง์ 
  - HTML์ DOM ์กฐ์๊ณผ ์ด๋ฒคํธ ์ ์ด, ์ ๋๋ฉ์ด์ ๊ทธ๋ฆฌ๊ณ  Ajax๊น์ง ์น ํ๋ฉด์ ๋ค๋ฃจ๋ ์๋ฐ์คํฌ๋ฆฝํธ ๋ผ์ด๋ธ๋ฌ๋ฆฌ
- ### ํ์ด์ง๋ค์ด์ ์ ์ฉ_*(1)*
  - `NavBar`๋ฅผ ์ด์ฉํ์ฌ  ์ผ์ ํ ํฌ๊ธฐ ๋ฏธ๋ง์ด ๋๋ฉด ๋ฉ๋ด์ฐฝ์ ๋์ฐ๊ฒ ํจ
  - `Bootstrp`์ ์ ์ฉํ๊ธฐ ์ํด `static` ๋๋ ํ ๋ฆฌ์ *[./static/bootstrap.min.js](./static/bootstrap.min.js)* ๋ฅผ ๋ฃ์ด๋ 
  - `NavBar` ์์ฑ์ด ๊ธธ๊ธฐ ๋๋ฌธ์ ๋ฐ๋ก `templates` ๋๋ ํ ๋ฆฌ์ ์ ์(*[./templates/navbar.html](./templates/navbar.html)*)
  -  [./templates/base.html](./templates/base.html)* ์ `navbar.html`์ **include**
   
        ```html
        <!--./templates/base.html-->
        <body>
            <!--navbar.html์ include ํ์ฌ ๋ถ๋ฌ์ด-->
            {% include 'navbar.html' %}
            <!--๊ณตํต ํํ๋ฆฟ-->
            <!--๋ธ๋ญ ๋ด์๋ง ๋ญ๊ฐ ๋ค์ด๊ฐ์ง ์ ๊ฒฝ์ฐ๋ฉด ๋๋ค-->
            <div class = "container my-3">
        <!--์๋ต-->
        ```
- ### ํ์ด์ง๋ค์ด์ ์ ์ฉ_*(2)*
  - ๊ฒ์๊ธ *๋ชฉ๋ก* ์ธํฐํ์ด์ค
  - **ํ์คํธ** ์ผ์ด์ค *์ฝ 300๊ฐ*๋ฅผ ์ถ๊ฐํจ
   
    ```python
    //./tests.py
    from yannjuApp.models import Question
    from django.utils import timezone

    for i in range(300):
        q = Question(
            subject = f'ํ์คํธ ๋ฐ์ดํฐ ์๋๋ค : [{i:03d}]',
            content = f'ํ์คํธ ๋ฐ์ดํฐ์ ๋ด์ฉ ์๋๋ค : [{i:03d}]',
            create_date = timezone.now()
        )
        q.save()
    ```
    - ์คํ์ํค๋ฉด ์๋์ ๊ฐ์ด 300๊ฐ์ ํ์คํธ ์ผ์ด์ค๊ฐ ๋ง๋ค์ด์ง
     
        ![ํ์คํธ ์ผ์ด์ค](../img/6_img(1).png)
  - `Page` ๊ฐ์ฒด๋ฅผ ์ด์ฉํ์ฌ ๊ด๋ฆฌ
  - `Pagination` ์ธํฐํ์ด์ค๋ฅผ ๋ง๋ค์ด์ `Page`๋ฅผ ํ์ด์ง ํ  ์ ์์
  - *[./templates/pagination.html](./templates/pagination.html)* ์ `Pagination` ์ธํฐํ์ด์ค๋ฅผ ์์ฑ
  - *[./yannjuApp/views.py](./yannjuApp/views.py)* ์ ํ์ด์ง ์ฒ๋ฆฌ๋ฅผ ์ํด `context` ๋ฅผ ์กฐ์ 
   
    ```python
    //yannjuApp/views.py
    //์๋ต
    #render๊ฐ return ํ๋๊ฒ body์ ๋ด์ฉ
        # question_list = Question.objects.order_by('-create_date')  #๋ด๋ฆผ์ฐจ์ = ์ต์ ๊ธ์ ์๋ก
        # context = {'question_list' : question_list} #key ์ ๋ช์นญ์ ํํ๋ฆฟ์์ ์ฌ์ฉํ  ๋ณ์ (= ์ปจํ์คํธ ๋ณ์)
        
        # ์๋ ฅ ํ๋ผ๋ฏธํฐ
        page = request.GET.get('page', '1') # ํ์ด์ง
        # ์กฐํ
        question_list = Question.objects.order_by('-create_date')
        # ํ์ด์ง์ฒ๋ฆฌ
        paginator = Paginator(question_list, 10) # ํ์ด์ง๋น 10๊ฐ์ฉ ๋ณด์ฌ์ฃผ๊ธฐ
        page_obj = paginator.get_page(page)
        context = {'question_list': page_obj}
    //ํ์์๋ต
    ```
      - ๊ธฐ์กด๊ณผ ๋ค๋ฅด๊ฒ `question_list`๋ฅผ **page** ๊ฐ์ฒด๋ก ์ค
  - *[./yannjuApp/views.py](./yannjuApp/views.py)*์์ ์ ์ํ `context`๋ฅผ ๋ฐํ์ผ๋ก ๋ชฉ๋ก ์ธํฐํ์ด์ค์ ๊ธฐ๋ฅ ๋ถ์ฌ
  - `add filter`, `paginator.has_next_number`, .. ์ ๊ฐ์ ๊ธฐ๋ฅ์ ์ฌ์ฉ
  - (์ฌ์ง์ถ๊ฐ~ํ๊ธฐ~)
- ### ๋ชฉ๋ก์ ์์๋ฒํธ ์กฐ์ 
  - ๊ฐ ํ์ด์ง(๋ชฉ๋กํ์ด์ง) ๋ณ `1` ๋ถํฐ ํ์ด์ง ๋ฒํธ๊ฐ ์์
- ### ์ธ๋ถ์์ ์ ๊ทผํ๊ธฐ
  - *[./config/settings.py](./config/settings.py)*์์ `ALLOWED_HOSTS` ์ ํ์ฌ `IP`๋ฅผ ์ถ๊ฐํ์ฌ ์ธ๋ถ์์ ์ ๊ทผ์ด ๊ฐ๋ฅํ๊ฒ ํจ
   
    ```python
    ALLOWED_HOSTS = ['172.30.1.93', '127.0.0.1', 'localhost']
    ```
  - ๋์ผํ `WiFi`๋ฅผ ์ฌ์ฉํ๋ ๊ฒฝ์ฐ ๊ฐ๋ฅ