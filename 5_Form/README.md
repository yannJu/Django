## 💫Form💫
- ### 질문 등록 버튼 만들기
  - `Form`을 이용하여 입력받기
  - *[./yannjuApp/forms.py](./yannjuApp/forms.py)* 에 class를 작성하고 `Question 객체`와 연결
   
    ```python
    class QuestionForm(forms.ModelForm):
        #Model에 대한것을 입력받아야하므로 Model에 대해 맞추겠다
        class Meta: #설명하는 데이터
            model  = Question
            fields = ['subject', 'content'] #진짜 연계를 시킬 데이터 -> id, date는 연계 X
    ``` 
  - `django`가 *field를* 이용하여 Question 객체와 **Mapping**시킴 
  - `질문등록`버튼을 클릭하면 다음과 같은 화면으로 넘어가게 된다.
   
   ![질문등록 화면](../img/5_img(1).png)