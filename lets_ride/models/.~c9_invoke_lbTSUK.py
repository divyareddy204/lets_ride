from django.db import models
from .user import User
from .shareride import ShareRide


class AssetTransportRequest(models.Model):
    
    asset_choices=(('parcel','parcel'),
                   ('bags','bags'),
                   ('others','others'))
    sensitivity_choices=(('HighlySensitive','HighlySensitive'),
                         ('Sensitive','Sensitive'),('Normal','normal'))
    
    
    source=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    flexible=models.BooleanField()
    datetime=models.DateTimeField(null=True)
    from_datetime=models.DateTimeField(null=True)
    to_datetime=models.DateTimeField(null=True)
    user=models.ForeignKey(User,related_name="asset_requested_person",
                           on_delete=models.CASCADE)
    no_of_assets=models.IntegerField(default=0)
    asset_type=models.CharField(max_length=100,choices=asset_choices)
    sensitivity=models.CharField(max_length=100,choices=sensitivity_choices)
    deliver_person=models.CharField(max_length=100)
    accepted_person=models.OneToOneField(ShareRide,related_name='asset_accepted_person', 
                                           on_delete=models.CASCADE)
    status = models.CharField(max_length=100, null=True)
