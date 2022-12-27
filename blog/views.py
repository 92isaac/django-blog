from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .form import Create_PostForm, Create_PostForm, Comment_PostForm
from .models import Story, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here

def home(request):
    all_story = Story.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(all_story, 3)
    try:
        story = paginator.page(page)
    except PageNotAnInteger:
        story = paginator.page(1)
    except EmptyPage:
        story = paginator.page(paginator.num_pages)
    context ={'story': story}
    return render(request, 'blog/home.html', context)



def profile(request, pk):
    story_id = Story.objects.get(id=pk)
    comment = Comment.objects.filter(story=story_id)
    count = comment.count()
    create_Post = Create_PostForm()
    create_comment = Comment_PostForm()
    
    if request.method == 'POST':
        post = Create_PostForm(request.POST)
        if post.is_valid():
            post.save()
            return redirect('profile/<str:pk>')
        
    if request.method == 'POST':
        make_comment =Comment_PostForm(request.POST)
        if make_comment.is_valid():
            make_comment.save()
            return redirect('home')
        
    context ={'story': story_id, 'comments': comment, 'count': count, 'create_post':create_Post, 'create_comment':create_comment}
    return render(request, 'blog/read_story.html', context)


def create_post(request):
    post = Create_PostForm()
    if request.method == 'POST':
        post = Create_PostForm(request.POST)
        if post.is_valid():
            post.save()
            return redirect('/')
    context = {'post': post,}
    return render(request, 'blog/makepost.html', context)



def update_blog_post(request, pk):
    blog_post_id = Story.objects.get(id=pk)
    blog_post = Create_PostForm(instance=blog_post_id)
    if request.method == 'POST':
        blog_post = Create_PostForm(request.POST, instance=blog_post_id)
        if blog_post.is_valid():
            blog_post.save()
            return redirect('/')
    context = {"blog_post": blog_post}
    return render(request, 'blog/update_blog_post.html', context)



def delete_post(request, pk):
    post_id = Story.objects.get(id=pk)
    post_id.delete()
    return redirect('/')


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')