from django.db import models

# Create your models here.
class Story(models.Model):
    # author
    title = models.CharField(max_length=255, blank=False)
    # img
    # comment = models.CharField()
    post = models.TextField(max_length=5000, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    id = models.IntegerField(auto_created=True, primary_key=True)


    def __str__(self):
        return self.title