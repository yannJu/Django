from django import forms
from yannjuApp.models import Question

class QuestionForm(forms.ModelForm):
    #Model에 대한것을 입력받아야하므로 Model에 대해 맞추겠다
    class Meta: #설명하는 데이터
        model  = Question
        fields = ['subject', 'content'] #진짜 연계를 시킬 데이터 -> id, date는 연계 X
        