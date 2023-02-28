from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer, Comment
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import QuestionForm, AnswerForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    '''
    yannjuApp 목록 출력 (doc string : 함수에서 가장 먼저 나온 문자열 : help를 제공하기 위한 용도로 주로 사용)
    '''
    #render가 return 하는게 body의 내용
    # question_list = Question.objects.order_by('-create_date')  #내림차순 = 최신글을 위로
    # context = {'question_list' : question_list} #key 의 명칭은 템플릿에서 사용할 변수 (= 컨텍스트 변수)
    
    # 입력 파라미터
    page = request.GET.get('page', '1') # 페이지
    # 조회
    question_list = Question.objects.order_by('-create_date')
    # 페이징처리
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    
    return render(request, 'yannjuApp/question_list.html', context)

def detail(request, question_id):
    '''
    yannjuApp 상세 출력
    '''
    # question = Question.objects.get(id = question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'yannjuApp/question_detail.html', context)

# def answer_create(request, question_id):
#     """
#     yannjuApp 답변등록
#     """
#     question = get_object_or_404(Question, pk=question_id)
#     question.answer_set.create(content=request.POST.get('content'), 
#     create_date=timezone.now()) 
#     return redirect('yannjuName:detail', question_id=question.id)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    """
    yannJuApp 게시글 질문 수정
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.auth:
        messages.error(request, '수정 권한이 없습니다. . 😅')
        return redirect('yannjuName:detail', question_id = question.id)
    
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question) #기존 데이터를 가져온 후 POST 데이터로 덮어씌움
        if form.is_valid():
            question = form.save(commit=False)
            # form.auth = request.user 이미 못들어오게 해놨기 때문에 없어도 됨
            question.modify_date = timezone.now()
            question.save()
            return redirect('yannjuName:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form' : form}
    return render(request, 'yannjuApp/question_form.html', context)

@login_required(login_url='common:login')
def question_create(request):
    """
    yannjuApp 질문등록
    """
    if request.method == 'POST': #POST 요청이라면 -> 저장하기 버튼
        form = QuestionForm(request.POST) #request.POST : 사전 형태로 데이터가 들어옴
        if form.is_valid():
            question = form.save(commit=False)
            question.auth = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('yannjuName:index')
    else: #GET 요청이라면 -> 질문등록버튼
        form = QuestionForm() #비어있는 데이터
    context = {'form':form}
    return render(request, 'yannjuApp/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    """
    yannjuApp 질문 삭제
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.auth:
        messages.error(request, '삭제 권한이 없습니다. . 😅')
        return redirect('yannjuName:detail', question_id = question.id)
    question.delete()
    return redirect('yannjuName:index')

@login_required(login_url='common:login') #Decorator 함수 -> 로그인이 되어있는지 먼저 유효성 체크
def answer_create(request, question_id):
    """
    yannjuApp 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.auth = request.user
            answer.create_date = timezone.now()
            answer.question = question #Foreign Key
            answer.save()
            return redirect("yannjuName:detail", question_id=question.id)
    else:
        form = AnswerForm()
    context =  {'question':question, 'form':form}
    return render(request, 'yannjuApp/question_detail.html', context)

@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    """
    yannjuApp 답변 수정
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if answer.auth != request.user:
        messages.error(request, '수정 권한이 없습니다. . 😅')
        return redirect('yannjuName:detail', answer_id = answer.id)
    
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.aith = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('yannjuName:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
        
    context = {'answer': answer, 'form': form}
    return render(request, 'yannjuApp/answer_form.html', context)

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    """
    yannjuApp 답변 삭제
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if answer.auth != request.user:
        messages.error(request, '삭제 권한이 없습니다. . 😅')
        return redirect('yannjuName:detail', answer_id = answer.id)
    answer.delete()
    return redirect('yannjuName:detail', question_id=answer.question.id)

#Comment Line-------------
#(1) Question
@login_required(login_url='common:login')
def comment_create_question(request, question_id):
    """
    yannjuApp 질문에 대한 댓글 추가
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.auth = request.user
            comment.create_date = timezone.now()
            comment.question = question
            comment.save()
            
            return redirect('yannjuName:detail', question_id = question.id)
    else:
        form = CommentForm()
        
    context = {'form' : form}
    return render(request, './yannjuApp/comment_form.html', context)

@login_required(login_url='common:login')
def comment_modify_question(request, comment_id):
    """
    yannjuApp 질문에 대한 댓글 수정
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.auth:
        messages.error(request, '수정 권한이 없습니다. . 😅')
        return redirect('yannjuName:detail', question_id = comment.question.id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.auth = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('yannjuName:detail', question_id = comment.question.id)
    else:
        form = CommentForm(instance=comment)
    
    context = {'form' : form}
    return render(request, 'yannjuApp/comment_form.html', context)
    
@login_required(login_url='common:login')
def comment_delete_question(request, comment_id):
    """
    yannjuApp 질문에 대한 댓글 삭제
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.auth:
        messages.error(request, '삭제 권한이 없습니다. . 😅')
        return redirect('yannjuName:detail', question_id = comment.question.id)
    else:
       comment.delete()
    return redirect('yannjuName:detail', question_id = comment.question.id)

#(1) Answer
@login_required(login_url='common:login')
def comment_create_answer(request, answer_id):
    """
    yannjuApp 답변에 대한 댓글 추가
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.auth = request.user
            comment.create_date = timezone.now()
            comment.answer = answer
            comment.save()
            
            return redirect('yannjuName:detail', question_id = answer.question.id)
    else:
        form = CommentForm()
    context = {'form' : form}
    
    return render(request, './yannjuApp/comment_form.html', context)

@login_required(login_url='common:login')
def comment_modify_answer(request, comment_id):
    """
    yannjuApp 답변에 대한 댓글 수정
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.auth:
        messages.error(request, '수정 권한이 없습니다. . 😅')
        return redirect('yannjuName:detail', question_id = comment.answer.question.id)
    
    if request.method == "POST":
        form = CommentForm(request.POST, instance = comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.auth = request.user
            comment.modify_date = timezone.now()
            comment.save()
            
            return redirect('yannjuName:detail', question_id=comment.answer.question.id)
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    
    return render(request, './yannjuApp/comment_form.html', context)

@login_required(login_url='common:login')
def comment_delete_answer(request, comment_id):
    """
    yannjuApp 답변에 대한 댓글 삭제
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.auth:
        messages.error(request, '삭제 권한이 없습니다. . 😅')
        return redirect('yannjuName:detail', question_id = comment.answer.question.id)
    else:
        comment.delete()
    return redirect('yannjuName:detail', question_id = comment.answer.question.id)