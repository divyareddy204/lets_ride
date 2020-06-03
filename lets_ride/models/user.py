from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_name = models.CharField(max_length=50, null=True)
    mobile_number = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
