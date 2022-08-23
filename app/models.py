from django.db import models
from django.core.validators import FileExtensionValidator


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class New(models.Model):
    category = models.ForeignKey(Category ,on_delete=models.CASCADE, blank=True, null=True)
    region = models.ForeignKey(Region ,on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    sumary = models.CharField(max_length=300, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    img = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
