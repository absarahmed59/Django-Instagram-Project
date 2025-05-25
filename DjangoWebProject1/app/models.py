"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Accounts(models.Model):
    username = models.CharField(max_length=64, primary_key=True)
    password = models.CharField(max_length=64)

class Profile(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    bio  = models.CharField(max_length=128)


class Posts(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    text = models.CharField(max_length=2048)
    likes = models.IntegerField()

class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    likes = models.IntegerField()
    text = models.CharField(max_length=128)


