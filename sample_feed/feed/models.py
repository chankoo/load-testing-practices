from django.db import models
from sample_feed.core.models import BaseModel


class FeedRecord(BaseModel):
    person = models.IntegerField()
    post = models.IntegerField()
    content = models.CharField(max_length=2000, default='')
    hide = models.BooleanField(default=False)

    class Meta:
        app_label = 'feed'
