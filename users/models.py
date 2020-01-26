from django.db import models
from django.contrib.auth.models import AbstractUser

class Uzivatel(AbstractUser):
    age = models.PositiveIntegerField(null=True,blank=True)

    class Meta:
        verbose_name = 'Uzivatel'
        verbose_name_plural = 'Uzivatelia'
