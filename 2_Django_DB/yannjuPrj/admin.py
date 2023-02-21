from django.contrib import admin
from .models import Question

# 검색기능을 위한 클래스
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject'] # 'subject'로 검색하겠다
    list_display = ['id', 'subject', 'create_date'] # 제시한 대로 list 를 표시
    ordering = ['id'] # id 기준으로 정렬 [-id]와 같이 음수 표현시 내림차순으로
    
admin.site.register(Question, QuestionAdmin)