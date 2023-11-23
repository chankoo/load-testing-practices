from django.db import models
from sample_feed.core.models import BaseModel


class PersonRelation(BaseModel):
    person = models.IntegerField(db_index=True)
    related_person = models.IntegerField()
    relation_type = models.CharField(max_length=10, default='friend')

    class Meta:
        app_label = 'feed'

    def __str__(self):
        return f"{self.related_person} is {self.relation_type} of mine({self.person})"
