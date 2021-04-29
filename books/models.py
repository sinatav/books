from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    _id = models.AutoField(primary_key=True)


class User(models.Model):
    username = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250)
    mobile = models.CharField(max_length=11)
    email = models.EmailField()
    isAdmin = models.BooleanField(default=False)
    token = models.CharField(max_length=250, default="")
    token_time = models.DateTimeField(auto_now=True)

