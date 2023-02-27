from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    # 파스칼 표기법에 의한 클래스 임을 알 수 있다.
    subject = models.CharField('제목', max_length=200)
    content = models.TextField('내용')
    create_date =  models.DateTimeField('날짜')
    auth = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.subject
    
class Answer(models.Model):
    # ForeignKey(참조테이블, 참조조건)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField('답변 내용')
    create_date = models.DateTimeField()
    auth = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.question.subject