from django.shortcuts import render, get_object_or_404, redirect
from ..models import Question
from django.utils import timezone
from ..forms import QuestionForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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