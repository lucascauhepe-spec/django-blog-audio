from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from .forms import PostForm
from .models import Post


def post_list(request):
    posts = Post.objects.filter(status=Post.Status.PUBLISHED).select_related("author")
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, slug):
    post = get_object_or_404(Post.objects.select_related("author"), slug=slug)
    if post.status != Post.Status.PUBLISHED and post.author != request.user:
        raise Http404
    return render(request, "blog/post_detail.html", {"post": post})

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            if post.status == Post.Status.PUBLISHED:
                messages.success(request, "Post published.")
            else:
                messages.success(request, "Draft saved. Only you can see it.")
            return redirect(post)
    else:
        form = PostForm()

    return render(request, "blog/post_form.html", {
        "form": form,
        "page_title": "New post",
        "button_text": "Save post",
    })
