from django.contrib import admin
from .models import Question, Answer

# 검색기능을 위한 클래스
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject'] # 'subject'로 검색하겠다
    list_display = ['id', 'subject', 'create_date'] # 제시한 대로 list 를 표시
    ordering = ['id'] # id 기준으로 정렬 [-id]와 같이 음수 표현시 내림차순으로
    
class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['question'] # 'subject'로 검색하겠다
    list_display = ['id', 'question', 'create_date'] # 제시한 대로 list 를 표시
    ordering = ['id'] # id 기준으로 정렬 [-id]와 같이 음수 표현시 내림차순으로
    
#site에 등록 
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)