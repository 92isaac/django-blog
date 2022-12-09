from django.shortcuts import render
# from django.http import HttpResponse
from .models import Story

# Create your views here

def home(request):
    story = Story.objects.all()
    context ={'story': story}
    return render(request, 'blog/home.html', context)

def profile(request, pk):
    story_id = Story.objects.get(id=pk)
    context ={'story': story_id}
    return render(request, 'blog/profile.html', context)