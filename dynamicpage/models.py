from django.db import models

# Create your models here.


class Page (models.Model):
    title = models.CharField (max_length=200)
    content = models.TextField ()


class Author (models.Model):
    name = models.CharField (max_length=200)


class Book (models.Model):
    title = models.CharField (max_length=200)
    authors = models.ManyToManyField (Author)