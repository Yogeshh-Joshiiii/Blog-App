from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # auto_now = True - will update the date posted to the current date time, every time the post was updated
    # auto_now_add = True - will update the date posted to the current time only when the post is been created but you cannot ever update the value of the date posted
    date_posted = models.DateTimeField(default = timezone.now)
    # with on_delete = models.CASCADE , when a user is deleted , all the posts related to that user also gets deleted
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    # how to find the url of a model object , is to create a get_absolute_url method in our model that return the path to the specific instances

    # redirect vs reverse 
    # reverse - simply returns the full URL to that route as a string 
    # redirect - will actually redirect you to a specific route 
    #here we want to return the URL as a string and elt the view handle the redirect for us.

    #import reverse function

    def get_absolute_url(self):
        # we have to provide the specific post with a primary key , for that we have to set the kwargs
        return reverse("post-detail",kwargs={"pk":self.pk})