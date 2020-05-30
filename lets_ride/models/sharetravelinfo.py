from django.db import models
from .user import User


class ShareTravelInfo(models.Model):

    medium_choices=(('Bus','Bus'),('Train','Train'),('Flight','Flight'))
    source=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    flexible=models.BooleanField()
    datetime=models.DateTimeField(null=True)
    from_datetime=models.DateTimeField(null=True)
    to_datetime=models.DateTimeField(null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    medium = models.CharField(max_length=100,choices=medium_choices)
    assets_quantity=models.IntegerField()
