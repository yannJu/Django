from django.urls import path
from . import views

app_name = 'yannjuName'

urlpatterns = [
    path('', views.index, name = 'index'),                                #목록보기
    path('<int:question_id>/', views.detail, name = 'detail'),    #상세보기
    path('answer/create/<int:question_id>/', views.answer_create, name = 'answer_create'), #답변 등록
    path('question/create/',views.question_create, name = "question_create"),           #질문 작성 버튼
]