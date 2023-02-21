from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone

# Create your views here.
def index(request):
    '''
    yannjuApp 목록 출력 (doc string : 함수에서 가장 먼저 나온 문자열 : help를 제공하기 위한 용도로 주로 사용)
    '''
    #render가 return 하는게 body의 내용
    question_list = Question.objects.order_by('-create_date')  #내림차순 = 최신글을 위로
    context = {'question_list' : question_list} #key 의 명칭은 템플릿에서 사용할 변수 (= 컨텍스트 변수)
    
    return render(request, 'yannjuApp/question_list.html', context)

def detail(request, question_id):
    '''
    yannjuApp 상세 출력
    '''
    # question = Question.objects.get(id = question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'yannjuApp/question_detail.html', context)

def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    #request.POST['content'] 를 쓸 때 값이 없으면 예외발생
    #request.POST.get('content') 를 쓸 때 값이 없으면  None 리턴
    question.answer_set.create(content=request.POST.get('content'), 
    create_date=timezone.now()) 
    return redirect('yannjuName:detail', question_id=question.id)