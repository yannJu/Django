## 💫Form💫
- ### 질문 등록 버튼 만들기
  - `Form`을 이용하여 입력받기
  - *[./yannjuApp/forms.py](./yannjuApp/forms.py)* 에 class를 작성하고 `Question 객체`와 연결
   
    ```python
    //yannjuApp/forms.py
    class QuestionForm(forms.ModelForm):
        #Model에 대한것을 입력받아야하므로 Model에 대해 맞추겠다
        class Meta: #설명하는 데이터
            model  = Question
            fields = ['subject', 'content'] #진짜 연계를 시킬 데이터 -> id, date는 연계 X
    ``` 
  - `django`가 *field를* 이용하여 Question 객체와 **Mapping**시킴 
  - `질문등록`버튼을 클릭하면 다음과 같은 화면으로 넘어가게 된다.
   
   ![질문등록 화면](../img/5_img(1).png)
   - `question/create` 화면으로 넘어갈때는 **GET** 메소드로 넘어가게 된다.
     - 해당화면에서 `저장하기` 버튼을 눌렀을 때는 **POST**로 넘어가고, 해당 화면은 **GET, POST** 둘다 받게 됨
     - 각 기능에 따라 *다르게* 처리해야한다.
- ### 같은 URL에서 다른 기능 처리
  ```python
  //yannjuApp/views.py
  def question_create(request):
    """
    yannjuApp 질문등록
    """
    if request.method == 'POST': #POST 요청이라면 -> 저장하기 버튼
        form = QuestionForm(request.POST) #request.POST : 사전 형태로 데이터가 들어옴
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('yannjuName:index')
    else: #GET 요청이라면 -> 질문등록버튼
        form = QuestionForm() #비어있는 데이터
    return render(request, 'yannjuApp/question_form.html', {'form':form})
  ```  
    - `request.method` 를 이용하여 **POST** 와 **GET**을 구분하여 기능을 나누어줌
    - `GET`요청인 경우 비어있는 `QuestionForm()`을 만들어줌
    - `POST`요청인 경우 데이터가 포함된 `QuestionForm()`을 **DB**에 저장