from django.db import models
from django.db.models.fields import TextField

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    body =models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title