# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth import login as auth_login, logout as auth_logout
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.models import User
# from .forms import PostForm, CommentForm, LoginForm, RegisterForm
# from .models import Post, Comment
# from django.contrib.auth.decorators import login_required


# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/post_list.html', {'posts': posts})

# def post_detail(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     comments = post.comments.all()
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect('post_detail', post_id=post.id)
#     else:
#         form = CommentForm()
#     return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})

# def post_create(request):
#     if not request.user.is_authenticated:
#         return redirect('login')
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect('post_list')
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_create.html', {'form': form})

# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             return redirect('post_list')
#     else:
#         form = LoginForm()
#     return render(request, 'blog/post_login.html', {'form': form})

# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = RegisterForm()
#     return render(request, 'blog/register.html', {'form': form})

# def logout(request):
#     auth_logout(request)
#     return redirect('post_list')


# @login_required
# def post_edit(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect('post_detail', post_id=post.pk) 
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form': form})

# @login_required
# def post_delete(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     if request.method == "POST":
#         post.delete()
#         messages.success(request, "Post deleted successfully.")
#         return redirect('post_list')
#     return render(request, 'blog/post_confirm_delete.html', {'post': post})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import PostForm, CommentForm, LoginForm, RegisterForm
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages 

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})

def post_create(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('post_list')
    else:
        form = LoginForm()
    return render(request, 'blog/post_login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('post_list')

@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully.")
            return redirect('post_detail', post_id=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect('post_list')
    return render(request, 'blog/post_delete.html', {'post': post})

