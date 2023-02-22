from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    #Model에 대한것을 입력받아야하므로 Model에 대해 맞추겠다
    class Meta: #설명하는 데이터
        model  = Question
        fields = ['subject', 'content'] #진짜 연계를 시킬 데이터 -> id, date는 연계 X
        
        # [1] widget 직접 설정
        # widgets = {
        #     'subject' : forms.TextInput(attrs={'class':'form-control'}),
        #     'content' : forms.Textarea(attrs={'class' : 'form-control', 'rows' : 10}),
        # }
        
        # 기존 모델에 label을 정의해 두었기 때문에 따로 정의하지 않아도 됨
        # label = {
        #     'subject' : '제목',
        #     'content' : '내용',
        # }
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']