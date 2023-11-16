from django.db import models
from sample_feed.core.models import BaseModel


class FeedRecord(BaseModel):
    owner = models.IntegerField()  # feed owner id
    person = models.IntegerField()  # author id
    post = models.IntegerField()  # post id
    content = models.CharField(max_length=2000, default='')
    hide = models.BooleanField(default=False)

    class Meta:
        app_label = 'feed'


class PersonRelation(BaseModel):
    person = models.IntegerField()
    related_person = models.IntegerField()
    relation_type = models.CharField(max_length=10, default='friend')

    class Meta:
        app_label = 'feed'

    def __str__(self):
        return f"{self.related_person} is {self.relation_type} of mine({self.person})"