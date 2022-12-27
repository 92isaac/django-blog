from django.forms import ModelForm
from .models import Story, Comment


class Create_PostForm(ModelForm):
    class Meta:
        model = Story
        fields = ['title','category','post', 'author']

class Comment_PostForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']