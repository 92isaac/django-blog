from django.forms import ModelForm
from .models import Story

class Create_Story(ModelForm):
    
    class Meta:
        model = Story
        fields = '__all__'