from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

class Todo(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(get_user_model(),on_delete = models.CASCADE,)
    done = models.BooleanField(default = False)

    def __str__(self):
        return self.title
