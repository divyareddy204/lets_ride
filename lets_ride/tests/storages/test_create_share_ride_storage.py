import pytest
from lets_ride.storages.storage_implementation \
    import StorageImplementation
from lets_ride.models import  ShareRide

@pytest.mark.django_db
def test_create_share_ride_creates_share_ride__object_with_given_details(create_users):
    
    #Arrange
    source = "hyderabad"
    destination = "bangloor"
    is_flexible= True
    datetime= None
    from_datetime = "2020-09-04 06:00:00.000000-08:00"
    to_datetime = "2020-09-05 06:00:00.000000-08:00"
    no_of_seats_available= 2
    assets_quantity=2
    user_id = 2
    storage = StorageImplementation()

    #Act
    storage.create_share_ride(
            source=source,
            destination=destination ,
            is_flexible=is_flexible,
            datetime=datetime,
            from_datetime=from_datetime,
            to_datetime=to_datetime,
            no_of_seats_available=no_of_seats_available,
            assets_quantity=assets_quantity,
            user_id = user_id
        )

    share_ride = ShareRide.objects.get(
        source=source,
        destination=destination ,
        is_flexible=is_flexible,
        datetime=datetime,
        from_datetime=from_datetime,
        to_datetime=to_datetime,
        user_id = user_id,
        no_of_seats_available=no_of_seats_available,
        assets_quantity=assets_quantity,
        )

    #Assert
    assert share_ride.no_of_seats_available == no_of_seats_available
    assert share_ride.assets_quantity == assets_quantity
