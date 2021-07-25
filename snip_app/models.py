from django.db import models
from django.core.validators import RegexValidator
import uuid
from django.contrib.auth.models import User


class Snip(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=40, default="Untitled")
    text = models.TextField()
    is_encrypted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.username + " : " + self.id

    def __unicode__(self):
        return self.id
