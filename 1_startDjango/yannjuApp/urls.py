# 앱단위로 url을 관리하기 위해 생성
from django.urls import path
from . import views

# urlpatterns 변수명 고정
urlpatterns = [
    path('', views.index), 
]
