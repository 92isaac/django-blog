from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Story
from .form import Create_Story

# Create your views here

def register(request):
    context={}
    return render(request, 'blog/register.html', context)

def home(request):
    story = Story.objects.all()
    context ={'story': story}
    return render(request, 'blog/home.html', context)

def profile(request, pk):
    story_id = Story.objects.get(id=pk)
    context ={'story': story_id}
    return render(request, 'blog/profile.html', context)


def create_story(request):
    form = Create_Story()
    if request.method == 'POST':
        form = Create_Story(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'storyform': form}
    return render(request, 'blog/create_story.html', context)