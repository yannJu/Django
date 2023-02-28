from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from ..models import Question, Answer, Comment
from django.utils import timezone
from ..forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
            
            url = resolve_url('yannjuName:detail', question_id = question.id)
            return redirect(f'{url}#comment_{comment.id}')
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
        
            url = resolve_url('yannjuName:detail', question_id = comment.question.id)
            return redirect(f'{url}#comment_{comment.id}')
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

    url = resolve_url('yannjuName:detail', question_id = comment.question.id)
    return redirect(url)

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
            
            url = resolve_url('yannjuName:detail', question_id = answer.question.id)
            return redirect(f'{url}#comment_{comment.id}')
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
            
            url = resolve_url('yannjuName:detail', question_id = comment.answer.question.id)
            return redirect(f'{url}#comment_{comment.id}')
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

    url = resolve_url('yannjuName:detail', question_id = comment.answer.question.id)
    return redirect(url)