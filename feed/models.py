from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class Person(BaseModel):
    username = models.CharField(max_length=50, default="")


class Post(BaseModel):
    author = models.ForeignKey("Person", on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"Post by {self.author.username} on {self.created_at}"
