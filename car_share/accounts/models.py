from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    user = models.ForeignKey(User, max_length=40)
    last_name = models.TextField(max_length=40)
    user_name = models.TextField(max_length=40)
    password = models.TextField(max_length=40)


