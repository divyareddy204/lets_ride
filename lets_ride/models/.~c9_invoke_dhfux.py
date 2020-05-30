from django.db import models
from .request import Request


class RideRequest(models.Model):

    request=models.OneToOneField(Request,on_delete=models.CASCADE)
    luggage_quantity=models.IntegerField()
