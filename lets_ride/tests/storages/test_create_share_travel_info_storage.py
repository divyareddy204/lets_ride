import pytest
from lets_ride.storages.storage_implementation \
    import StorageImplementation
from lets_ride.models import  ShareTravelInfo
from lets_ride.constants.enums import MediumType

@pytest.mark.django_db
def test_create_share_travel_info_creates_share_travel_info_object_with_given_details(create_users):
    
    #Arrange
    source = "hyderabad"
    destination = "bangloor"
    flexible= True
    datetime= None
    from_datetime = "2020-09-04 06:00:00.000000-08:00"
    to_datetime = "2020-09-05 06:00:00.000000-08:00"
    assets_quantity=2
    medium = MediumType.Bus.value
    user_id = 4
    storage = StorageImplementation()

    #Act
    storage.create_share_travel_info(
            source=source,
            destination=destination ,
            flexible=flexible,
            datetime=datetime,
            from_datetime=from_datetime,
            to_datetime=to_datetime,
            medium=medium,
            assets_quantity=assets_quantity,
            user_id = user_id
        )

    share_travel_info = ShareTravelInfo.objects.get(
        source=source,
        destination=destination ,
        flexible=flexible,
        datetime=datetime,
        from_datetime=from_datetime,
        to_datetime=to_datetime,
        user_id = user_id,
        medium=medium,
        assets_quantity=assets_quantity,
        )

    #Assert
    assert share_travel_info.medium == medium
    assert share_travel_info.assets_quantity == assets_quantity
