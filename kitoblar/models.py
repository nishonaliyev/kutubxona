import time

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    text = models.TextField(blank=True)
    author = models.CharField(max_length=100, blank=True)
    isbn = models.CharField(max_length=13, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, blank=True)

    def __str__(self):
        return self.title





class Comment(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.author}"

class Like(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

