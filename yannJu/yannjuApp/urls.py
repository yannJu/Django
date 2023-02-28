from django.urls import path
from . import views

app_name = 'yannjuName'

urlpatterns = [
    path('', views.index, name = 'index'),                                #목록보기
    path('<int:question_id>/', views.detail, name = 'detail'),    #상세보기
    # Answers
    path('answer/create/<int:question_id>/', views.answer_create, name = 'answer_create'), #답변 등록
    path('answer/modify/<int:answer_id>', views.answer_modify, name='answer_modify'),       #답변 수정
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),      # 답변 삭제
    # Questions
    path('question/create/',views.question_create, name = "question_create"),           #질문 작성 버튼
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),          #질문 수정 버튼
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),          #질문 삭제
    #Comment
    # --- Question Comment
    path('comment/create/question/<int:question_id>/', views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', views.comment_delete_question, name='comment_delete_question'),
    # --- Answer Comment
    path('comment/create/answer/<int:answer_id>/', views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', views.comment_delete_answer, name='comment_delete_answer'),
    
]