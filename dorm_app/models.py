from django.db import models


# Create your models here.

# class Meta:
#     model = 'search.User'
#     fields = ("username",)

class Search(models.Model):
    search = models.CharField(max_length=200)

    def __str__(self):
        return self.search

class Advice(models.Model):
    title = models.CharField(max_length=200, default = 'SOME STRING')
    body = models.TextField()

    def __str__(self):
        return self.title
