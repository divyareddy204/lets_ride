from django.db import models
from .user import User


class ShareRide(models.Model):

    source=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    flexible=models.BooleanField()
    datetime=models.DateTimeField(null=True)
    from_datetime=models.DateTimeField(null=True)
    to_datetime=models.DateTimeField(null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    assets_quantity=models.IntegerField()
    no_of_seats_available=models.IntegerField()
