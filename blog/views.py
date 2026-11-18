from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm, SearchForm
from .models import Post


def post_list(request):
    posts = Post.objects.filter(status=Post.Status.PUBLISHED).select_related("author")
    form = SearchForm(request.GET or None)
    query = ""

    if form.is_valid():
        query = form.cleaned_data["q"]
        if query:
            posts = posts.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )

    return render(request, "blog/post_list.html", {
        "posts": posts,
        "form": form,
        "query": query,
    })


def post_detail(request, slug):
    post = get_object_or_404(Post.objects.select_related("author"), slug=slug)
    if post.status != Post.Status.PUBLISHED and post.author != request.user:
        raise Http404
    return render(request, "blog/post_detail.html", {"post": post})


@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
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


@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated.")
            return redirect(post)
    else:
        form = PostForm(instance=post)

    return render(request, "blog/post_form.html", {
        "form": form,
        "post": post,
        "page_title": "Edit post",
        "button_text": "Save changes",
    })


@login_required
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted.")
        return redirect("blog:post_list")

    return render(request, "blog/post_confirm_delete.html", {"post": post})