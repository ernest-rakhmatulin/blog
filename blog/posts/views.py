from django.shortcuts import render
from .models import Post

from django.http import HttpResponse
import datetime


def my_first_view(request):
    articles = Post.objects.filter(
        date_publish__lte=datetime.datetime.now()
    )

    return render(request, 'index.html', {
        'articles': articles
    })