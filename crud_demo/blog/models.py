from django.db import models
from django.contrib.auth.models import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)

    def __str__(self):
        return self.title
