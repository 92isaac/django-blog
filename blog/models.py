from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Story(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    img = models.ImageField(default='/media/default.png', upload_to='blogpost_img')
    politics = 'politics'
    tech = 'tech'
    religion = 'religion'
    sport = 'sport'
    other = 'other'
    category_choices = [(politics, 'politics'), (tech, 'tech'), (religion, 'religion'), (sport, 'sport'), (other, 'other')]
    category =models.CharField(max_length=10, choices=category_choices, default=other)
    post = models.TextField(max_length=5000, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-date_updated', '-date_created']


    def __str__(self):
        return self.title
    


class Comment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:50]
