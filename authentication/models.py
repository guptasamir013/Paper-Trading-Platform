from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    occupation = models.CharField(max_length=100, null=True)
    balance = models.IntegerField(default=None, null=True)
