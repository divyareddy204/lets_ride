import pytest
from lets_ride.storages.storage_implementation \
    import StorageImplementation
from lets_ride.models import  AssetTransportRequest
from lets_ride.constants.enums import AssetType, SensitivityType

@pytest.mark.django_db
def test_create_asset_transport_request_creates_asset_transport_request_object_with_given_details(create_users):
    
    #Arrange
    source = "hyderabad"
    destination = "bangloor"
    flexible= True
    datetime= None
    from_datetime = "2020-09-04 06:00:00.000000-08:00"
    to_datetime = "2020-09-05 06:00:00.000000-08:00"
    no_of_assets= 2
    asset_type = AssetType.parcel.value
    sensitivity = SensitivityType.HighlySensitive.value
    deliver_person = "ram"
    user_id = 4
    storage = StorageImplementation()

    #Act
    storage.create_asset_transport_request(
            source=source,
            destination=destination ,
            flexible=flexible,
            datetime=datetime,
            from_datetime=from_datetime,
            to_datetime=to_datetime,
            no_of_assets=no_of_assets,
            asset_type=asset_type,
            sensitivity=sensitivity,
            deliver_person=deliver_person,
            user_id = user_id
        )

    asset_transport_request = AssetTransportRequest.objects.get(
        source=source,
        destination=destination ,
        flexible=flexible,
        datetime=datetime,
        from_datetime=from_datetime,
        to_datetime=to_datetime,
        user_id = user_id,
        no_of_assets=no_of_assets,
        asset_type=asset_type,
        sensitivity=sensitivity,
        deliver_person=deliver_person,
        )

    #Assert
    assert asset_transport_request.no_of_assets == no_of_assets
    assert asset_transport_request.sensitivity == sensitivity

