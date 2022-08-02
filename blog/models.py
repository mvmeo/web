from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from ckeditor.fields import RichTextField
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.CharField(max_length=150, default='')
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse("home")
    