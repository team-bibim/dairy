from django.db import models
from django.utils import timezone

class Diary(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title