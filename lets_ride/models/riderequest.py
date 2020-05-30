from django.db import models
from .user import User
from .shareride import ShareRide


class RideRequest(models.Model):

    source=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    flexible=models.BooleanField()
    datetime=models.DateTimeField(null=True)
    from_datetime=models.DateTimeField(null=True)
    to_datetime=models.DateTimeField(null=True)
    user=models.ForeignKey(User,related_name="ride_requested_person", 
                                        on_delete=models.CASCADE)
    no_of_seats=models.IntegerField(default=0)
    luggage_quantity=models.IntegerField(default=0)
    accepted_person = models.ForeignKey(User,related_name='ride_accepted_person', 
                                        on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=100, null=True)
