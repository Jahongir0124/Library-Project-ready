from django.db import models
from books.models import *
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/photoUsers')


    def __str__(self):
        return self.user.username

