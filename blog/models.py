from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class Category(models.Model):
#     name = models.CharField(max_length=255, blank=False, null=True)

#     def __str__(self):
#         return self.name
    


class Story(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, blank=False)
    # img
    politices = "politices"
    sport = "sport"
    christain ='christain'
    tech ='tech'
    others = "others"
    category_choices = [(christain, 'christain'), (sport, 'sport'), (politices, 'politics'),(tech, 'tech'), (others, 'others')]
    category = models.CharField(max_length=10, choices=category_choices, default=christain)
    post = models.TextField(max_length=5000, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    # id = models.IntegerField(auto_created=True, primary_key=True)


    def __str__(self):
        return self.title
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, null=True)
    body =models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.body[0:50]
