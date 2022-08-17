from django.db import models
from user.models import User
# Create your models here.


class Note(models.Model):
    title = models.CharField('title', max_length=100)
    content = models.TextField('content')
    created_time = models.DateTimeField('created_time', auto_now_add=True)
    updated_time = models.DateTimeField('updated_time', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
