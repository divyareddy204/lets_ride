import pytest
from unittest.mock import create_autospec
from lets_ride.interactors.create_ride_request_interactor \
    import CreateRideRequestInteractor
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface

def test_ride_request_creates_ride():
    
    #Arrange
    source = "hyderabad"
    destination = "bangloor"
    flexible= True
    datetime= ""
    from_datetime = "2020,5,28,20,00,00"
    to_datetime = "2020,5,29,09,00,00"
    no_of_seats= 2
    luggage_quantity=2
    user_id =1

    storage = create_autospec(PostStorageInterface)
    
    presenter = create_autospec(PresenterInterface)
    interactor = CreateRideRequestInteractor(
        storage = storage,
        presenter = presenter
        )

    #act
    interactor.create_ride_request(
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

    #assert
    storage.create_ride_request.assert_called_once_with(source=source,
            destination=destination ,
            flexible=flexible,
            datetime=datetime,
            from_datetime=from_datetime,
            to_datetime=to_datetime,
            no_of_seats=no_of_seats,
            luggage_quantity=luggage_quantity,
            user_id=user_id)
