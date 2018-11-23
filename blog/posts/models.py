from django.contrib.auth import get_user_model
from django.db import models
import datetime

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False, null=False)
    parent = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Post(models.Model):

    class Meta:
        ordering = ['-date_created']

    title = models.CharField(max_length=150)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_publish = models.DateTimeField(blank=True, null=False, default=datetime.datetime.now())
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

