from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField('username', max_length=11)
    password = models.CharField('password', max_length=32)
    created_time = models.DateTimeField('created_time', auto_now_add=True)
    updated_time = models.DateTimeField('updated_time', auto_now=True)

    def __str__(self):
        return 'username: ' + self.username
