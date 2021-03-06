from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_name = models.CharField(max_length=50)
    name
    #mobile_number = models.CharField(max_length=50)

    def __str__(self):
        return "%s %s" % (self.name, self.user_name)
