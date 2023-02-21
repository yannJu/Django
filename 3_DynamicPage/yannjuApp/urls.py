from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),                                #목록보기
    path('<int:question_id>/', views.detail),    #상세보기
]
