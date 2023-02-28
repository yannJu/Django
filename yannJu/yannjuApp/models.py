from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    # 파스칼 표기법에 의한 클래스 임을 알 수 있다.
    subject = models.CharField('제목', max_length=200)
    content = models.TextField('내용', help_text='비방, 욕설 및 도배글은 삭제될 수 있습니다- (/▽＼)')
    create_date =  models.DateTimeField('날짜')
    auth = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='author_question') #에 의해 `question_set`이라는 관계매니저가 생겼었음
    modify_date = models.DateTimeField(null=True, blank=True)
    
    # User : 참조, `question_set` 이라는 관계매니저가 다시 생김, auth와 충돌 / 따라서 related_name 을 통해 해결
    voter = models.ManyToManyField(User, related_name='voter_question') 
    
    def __str__(self):
        return self.subject
    
class Answer(models.Model):
    # ForeignKey(참조테이블, 참조조건)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField('답변 내용')
    create_date = models.DateTimeField()
    auth = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='author_answer')
    modify_date = models.DateTimeField(null=True, blank=True)
    
    voter = models.ManyToManyField(User, related_name='voter_answer') 
    
    def __str__(self):
        return self.question.subject
    
class Comment(models.Model):
    auth = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField('댓글 내용')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)