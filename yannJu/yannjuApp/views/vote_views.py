from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Question, Answer

@login_required(login_url="common:login")
def vote_question(request, question_id):
    """
    yannjuApp 추천 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if (request.user == question.auth):
        messages.error(request, "본인이 작성한 글은 추천할 수 없습니다🥵")
    else:
        question.voter.add(request.user) # 중요 ! -> n:m 관계에 추가
        
    return redirect('yannjuName:detail', question_id = question.id)

@login_required(login_url='common:login')
def vote_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    
    if request.user == answer.auth:
        messages.error(request, "본인이 작성한 답변은 추천할 수 없습니다🥵")
    else:
        answer.voter.add(request.user)
    
    return redirect('yannjuName:detail', question_id = answer.question.id)