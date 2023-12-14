from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required

@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            return redirect('show_posts')
    else:
      post_form = forms.PostForm()

    return render(request, 'posts/add_post.html', {'form1': post_form})


@login_required
def edit_post(request, id):
    post = models.PostModel.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('show_posts')

    return render(request, 'posts/add_post.html', {'form1': post_form})


@login_required
def detete_post(request, id):
    try:
        post = models.PostModel.objects.get(pk=id)
        post.delete()
        return redirect('show_posts')
    except models.PostModel.DoesNotExist:
        return render(request, 'posts/task_not_found.html', {'id': id})