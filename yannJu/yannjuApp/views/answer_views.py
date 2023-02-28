from django.shortcuts import render, get_object_or_404, redirect
from ..models import Question, Answer
from django.utils import timezone
from ..forms import  AnswerForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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