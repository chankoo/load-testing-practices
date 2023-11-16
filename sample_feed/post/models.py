from django.db import models
from sample_feed.core.models import BaseModel


class Person(BaseModel):
    username = models.CharField(max_length=50, default="")

    class Meta:
        app_label = 'post'


class Post(BaseModel):
    person = models.IntegerField(null=True, blank=True)
    content = models.CharField(max_length=2000, default='')

    class Meta:
        app_label = 'post'

    def __str__(self):
        return f"Post by {self.person} on {self.created_at}"
