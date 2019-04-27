from django.contrib.auth.models import models, User
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=100, default='sample title')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

