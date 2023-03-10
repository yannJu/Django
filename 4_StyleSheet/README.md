## ๐ซStyleSheet๐ซ
- ### *์ ์  ํ์ผ* ์ฒ๋ฆฌ
  - *[config/settings](./config/settings.py)* ์์ `STATICFILES_DIRS - [
    BASE_DIR / 'static',
]` ์ ์์ฑ โ ์ด๋ BASE_DIR ํ์๋ก ์ง์ 
  - ์ฌ๋ฌ๊ฐ๋ฅผ ์ง์ ํ  ์ ์๋ค.
  - ํ๋ก์ ํธ **root**์ `static`ํด๋ ์์ฑ : django๋ฅผ ๊ฑฐ์น์ง ์๊ณ  ๋ฐ๋ก ํด๋์ ์ ๊ทผํจ
- ### ์นํ์ด์ง์ `StyleSheet` ์ ์ฉ
  - `static`ํ์์ *[static/style.css](./static/style.css)* ์ ์์ฑํ์ฌ *StyleSheet* ์์ฑ
  - *[tmplates/yannjuApp/question_detail.html](./tmplates/yannjuApp/question_detail.html)* ์์ ์ธ๋ถ css ํ์ผ์ `link`๋ฅผ ์ด์ฉํ์ฌ ๋ถ๋ฌ์ด

    ```html
    <!--tmplates/yannjuApp/question_detail.html-->
    {% load static %} <!--static lib์ ์ฌ์ฉํจ์ ์๋ฏธ-->
    <link rel = "stylesheet" type = "text/css" href = "{% static 'style.css' %}">
    ```
  - `{% load static %}` ์ ํธ์ถํ์ฌ ์ดํ ์์์น ๋ชปํ๊ฒ `static`์ ๊ฒฝ๋ก๊ฐ ๋ฐ๋๋ ๊ฒฝ์ฐ๋ฅผ ๋๋น
    - ๋ฐ๋ผ์ `href`์ ๋ง์น *URL๋ณ์นญ*์ ๋ฌ๋ฏ `static` ๋ง์ ์ฌ์ฉํ์ฌ ํด๊ฒฐ
- ### `BootStrap` ์ ์ด์ฉํ๊ธฐ
  - ์ํ๋ css ํ์ผ์ ์ฌ์ฉ(*[./static/bootstrap.min.css](./static/bootstrap.min.css)*)
    ```html
    <!--tmplates/yannjuApp/question_list.html-->
    {% load static %} <!--static lib์ ์ฌ์ฉํจ์ ์๋ฏธ-->
    <link rel = "stylesheet" type = "text/css" href = "{% static 'bootstrap.min.css' %}">
    ``` 
    - `href`๋ฅผ ` bootstrap.min.css`๋ก ์์ฑ
  - ํ๊ทธ๋ฅผ ํตํ์ฌ style sheet ์ ์ฉ(*[./templates/yannjuApp/question_list.html](./templates/yannjuApp/question_list.html)*)
   
    ```html
    <!--tmplates/yannjuApp/question_list.html-->
    <div class = "container my-3">
            <table class = 'table table-hover'>
                <thead>
                    <tr class = "thead-dark">
                        <th>๋ฒํธ</th>
                        <th>์ ๋ชฉ</th>
                        <th>์์ฑ์ผ์</th>
                    </tr>
                </thead>
            <!-- ( ์๋ต ) -->
        </table>
    </div>
    ```
    - `my -3` : **m**argin **y**์ขํ **3**๋งํผ 
    - `container` : container์ฒ๋ผ ๋ฌถ๊ณ  ๊ฐ์ด๋ฐ์ ๋์์ค
    - `table-hover` : **๋ง์ฐ์ค๋ฅผ** ๋ชฉ๋ก์ ๋๋ฉด ์ปฌ๋ฌ **์ด๋ฒคํธ** ๋์
    - `thead-dark` : thead ๋ฅผ **dark** ์ปฌ๋ฌ๋ก ๋ณ๊ฒฝ
     
    ![bootstrapImg](../img/4_img(1).png) 
  - ํ์ ๋ชฉ๋ก ๋ํ **ํ์ด๋ธ๋ก** ๊ตฌ์ฑ, *ํญ ๋๋น ๋์ด์ง*
  - ๊ทธ ์ธ์๋ `flex`, `badge`, `white-space`, `card`, . . ๋ฑ์ด ์์
- ### MTV (Model Template View)
  - ๊ด์ฌ์ฌ๋ฅผ *๋ถ๋ฆฌ*ํ์ฌ **๋ณต์ก๋**๋ฅผ *๋ฎ์ถ๊ณ * ๊ด๋ฆฌ ๋ฐ ์ ์ง๋ณด์๊ฐ ๊ฐ๋ฅํด์ง
  - `Model` : ๋ฐ์ดํฐ ์ฒ๋ฆฌ
  - `Template` : ํํ (presentation - html)
  - `View` : ๋ฐ์ดํฐ ๊ฐ๊ณต
-  ### ์ฝ๋ ์ค๋ณต ํด๊ฒฐ
   -  *[./static/bootstrap.min.css](./static/bootstrap.min.css)* ํ์ผ์ *[templates](./templates/)* ํ์ ํ์ผ๋ค์์ ์ฌ์ฉํ๊ฒ ๋๋๋ฐ ๋ง์ฝ ๊ทธ ํ์ ํ์ผ์ด *๋งค์ฐ ๋ง์ ๊ฒฝ์ฐ* **์ฝ๋ ์ค๋ณต** ๋ฐ์
   -  ๋ฐ๋ผ์ **HTML**๊ณผ **ํํ๋ฆฟ ์์** ์ ํตํด ํด๊ฒฐ
      -  *[./templates/base.html](./templates/base.html)* ์ HTML ๋ฌธ์ ์์ฑ
      -  `bootstrap.min.css`์ ์์น๋ฅผ `base.html`์ ์์ฑํ์ฌ ์ฝ๋ ์ค๋ณต ํด๊ฒฐ
      -  `body`๋ด์ `block`๋ฌธ๋ง ์ ๊ฒฝ์ฐ๋ฉด ๋๋ค.
      -  ์ดํ ๋ค๋ฅธ StyleSheet templates Html ๋ค ์๋จ์ extends ์์ฑ, block ๋ฌธ ๋ด๋ถ๋ก ์ด๋์ํด
        
          ```html
          <!--./templates/yannjuApp/question_list.html-->
          {% extends 'base.html' %}

          <div class = "container my-3">
            {% block content %}
            <!--์๋ต-->
            {% endblock content %}
          </div>
          ```
        - ๋ํ *[./templates/yannjuApp/question_detail.html](./templates/yannjuApp/question_detail.html)*  ์ *[./templates/yannjuApp/question_list.html](./templates/yannjuApp/question_list.html)*  ์  ๋ชจ๋ ์ ์ฒด์ ์ผ๋ก `<div container>` ๋ก ๊ฐ์ธ์ ธ ์์ผ๋ฏ๋ก **๊ณตํต block**  ์ผ๋ก ๋นผ๋ด์ด ์ฌ์ฉ
         
          ```html
          <!--templates/base.html-->
          <div class = "container my-3">
              {% block content %}{% endblock content %}
          </div>
          ``` 
 - ### `CDN`์ ์ด์ฉํ์ฌ ์์ด์ฝ ์ฌ์ฉ
   - `font awesome cdn`์ ํตํด **์์ด์ฝ์** ์ฌ์ฉ
   - ์์ด์ฝ **ํฐํธ** ์ด๊ธฐ ๋๋ฌธ์ *๊ธ์์ฒ๋ผ* ์ฌ์ฉ ๊ฐ๋ฅ
   - *[./templates/base.html](./templates/base.html)* ์ `font awesome cdn` ํ๊ทธ๋ฅผ ์ถ๊ฐ
   - `font awesome`์์ ์ํ๋ ์์ด์ฝ์ ์ ํํ์ฌ ํ๊ทธ ์ถ๊ฐ
    
    ![์ด๋ฏธ์ง ์๋ก๋](../img/4_img(2).png) 