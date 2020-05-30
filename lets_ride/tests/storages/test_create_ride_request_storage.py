import pytest
from lets_ride.storages.storage_implementation \
    import StorageImplementation
from lets_ride.models import RideRequest

@pytest.mark.django_db
def test_create_ride_request_creates_ride_request_object_with_given_details(create_users):
    
    #Arrange
    source = "hyderabad"
    destination = "bangloor"
    flexible= True
    datetime= None
    from_datetime = "2020-09-04 06:00:00.000000-08:00"
    to_datetime = "2020-09-05 06:00:00.000000-08:00"
    no_of_seats= 2
    luggage_quantity=2
    user_id = 4
    storage = StorageImplementation()

    #Act
    storage.create_ride_request(
            source=source,
            destination=destination ,
            flexible=flexible,
            datetime=datetime,
            from_datetime=from_datetime,
            to_datetime=to_datetime,
            no_of_seats=no_of_seats,
            luggage_quantity=luggage_quantity,
            user_id = user_id
        )
    ride_request = RideRequest.objects.get(
        no_of_seats=no_of_seats,
        luggage_quantity=luggage_quantity,
        source=source,
        destination=destination ,
        flexible=flexible,
        datetime=datetime,
        from_datetime=from_datetime,
        to_datetime=to_datetime,
        user_id = user_id
        )

    #Assert
    assert ride_request.no_of_seats == no_of_seats
    assert ride_request.luggage_quantity == luggage_quantity

