from django.shortcuts import render, HttpResponse

# Create your views here.
# 함수내에 매개변수는 필수 . . . 
def index(request):
    # HttpResponse : 클래스 이므로 매개변수는 생성자에 들어감
    # 매개변수는 body 의 내용이라고 할 수 있음.
    return HttpResponse("안녕하세욤 'ㅅ ' 저는 얀조입니다 - ")