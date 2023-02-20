"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 사용자가 추가 하지 않고 admin만 있는 경우 기본 default 화면이 나옴
    # url이 많아지면 관리가 좋아지지 않음 -> 앱 단위로 분리시키자
    # path('yannjuApp/', views.index), 가 아니라 아래처럼 분리 + include 호출
    path('yannjuApp/', include('yannjuApp.urls')),
]
