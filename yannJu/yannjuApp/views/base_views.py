from django.shortcuts import render, get_object_or_404
from ..models import Question
from django.core.paginator import Paginator
from django.db.models import Q

def index(request):
    '''
    yannjuApp 목록 출력 (doc string : 함수에서 가장 먼저 나온 문자열 : help를 제공하기 위한 용도로 주로 사용)
    '''
    #render가 return 하는게 body의 내용
    # question_list = Question.objects.order_by('-create_date')  #내림차순 = 최신글을 위로
    # context = {'question_list' : question_list} #key 의 명칭은 템플릿에서 사용할 변수 (= 컨텍스트 변수)
    
    # 입력 파라미터
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') #검색 설정
    # 조회
    question_list = Question.objects.order_by('-create_date')
    
    # 검색이 이루어진다면
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains = kw) | #제목 검색
            Q(content__icontains = kw) | #내용 검색
            Q(auth__username__contains=kw) | #질문 글쓴이 검색
            Q(answer__auth__username__icontains=kw)  #답글 검색
        ).distinct()
    # 페이징처리
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {
        'question_list': page_obj, 
        'page' : page,
        'kw' : kw,
    }
    
    return render(request, 'yannjuApp/question_list.html', context)

def detail(request, question_id):
    '''
    yannjuApp 상세 출력
    '''
    # question = Question.objects.get(id = question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'yannjuApp/question_detail.html', context)