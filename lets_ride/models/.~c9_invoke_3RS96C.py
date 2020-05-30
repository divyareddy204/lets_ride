from django.db import models
from .travel_info import TravelInfo


class AssetTransportRequest(models.Model):
    
    asset_choices=(('parcel','parcel'),('bags','bags'),('others','others'))
    sensitivity_choices=(('HighlySensitive','HighlySensitive'),('Sensitive','Sensitive'),('Normal','normal'))
    
    
    no_of_assets=models.IntegerField(default=Tr)
    destination=models.CharField(max_length=100)
    flexible=models.BooleanField()
    datetime=models.DateTimeField(null=True)
    from_datetime=models.DateTimeField(null=True)
    to_datetime=models.DateTimeField(null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    no_of_assets=models.IntegerField(default=0)
    asset_type=models.CharField(max_length=100,choices=asset_choices)
    sensitivity=models.CharField(max_length=100,choices=sensitivity_choices)
    deliver_person=models.CharField(max_length=100)