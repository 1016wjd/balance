from django.shortcuts import render, redirect
from .models import Poll, Comment
from .forms import PostForm, CommentForm

# Create your views here.


def index(request):
    polls = Poll.objects.all()
    comment_form = CommentForm() 

    context = {
        'polls': polls,
        'comment_form': comment_form,
    }
   
    return render(request, 'index.html', context)


def comment(request, poll_id):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.poll_id = poll_id
            comment.save()
            return redirect('polls:index')
    
