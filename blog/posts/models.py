from django.db import models

# Create your models here.


class Post(models.Model):

    class Meta:
        ordering = ['-date_created']

    title = models.CharField(max_length=150)
    text = models.TextField()
    date_created = models.DateTimeField(auto_created=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title