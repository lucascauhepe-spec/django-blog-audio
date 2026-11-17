from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from blog.models import Post

from .forms import ProfileForm, SignUpForm


def signup(request):
    if request.user.is_authenticated:
        return redirect("blog:post_list")

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("blog:post_list")
    else:
        form = SignUpForm()

    return render(request, "registration/signup.html", {"form": form})


@login_required
def profile(request):
    posts = request.user.posts.all()
    drafts = posts.filter(status=Post.Status.DRAFT)
    published = posts.filter(status=Post.Status.PUBLISHED)

    return render(request, "accounts/profile.html", {
        "drafts": drafts,
        "published": published,
    })


@login_required
def profile_edit(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect("accounts:profile")
    else:
        form = ProfileForm(instance=request.user)

    return render(request, "accounts/profile_form.html", {"form": form})