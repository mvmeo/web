from distutils.command.upload import upload
from hashlib import blake2b
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Post(models.Model):


    class Category(models.TextChoices):
        BLOG = 'Blog', _('Blog')
        NOTAS = 'Notas', _('Notas')
    
    class Location(models.TextChoices):
        SANTIAGO = 'Santiago, Chile', _('Santiago, Chile')
        RANCAGUA = 'Rancagua, Chile', _('Rancagua, Chile')

    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    title = models.CharField(max_length=255)
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.BLOG,
    )
    location = models.CharField(
        max_length=20,
        choices=Location.choices,
        default=Location.SANTIAGO,
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='samuel')
    resume = models.TextField(default='')
    body = models.TextField(default='')
    post_date = models.DateField(auto_now_add=True)

    
    

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse("home")
    