from django.db import models
from sample_feed.core.models import BaseModel


class Person(BaseModel):
    username = models.CharField(max_length=50, default="")

    class Meta:
        app_label = 'post'


class Post(BaseModel):
    author = models.ForeignKey("Person", on_delete=models.CASCADE)
    content = models.TextField()

    class Meta:
        app_label = 'post'

    def __str__(self):
        return f"Post by {self.author.username} on {self.created_at}"
