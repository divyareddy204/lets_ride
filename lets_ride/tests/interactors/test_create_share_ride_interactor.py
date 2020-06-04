import pytest
from unittest.mock import create_autospec
from lets_ride.interactors.create_share_ride_interactor import CreateShareRideInteractor
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface

def test_share_ride_creates_share_object():
    
    
    source = "hyderabad"
    destination = "bangloor"
    is_flexible= True
    datetime= ""
    from_datetime = "2020,5,28,20,00,00"
    to_datetime = "2020,5,29,09,00,00"
    no_of_seats_available= 2
    assets_quantity=2
    user_id =1

    storage = create_autospec(PostStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateShareRideInteractor(
        storage = storage,
        presenter = presenter
        )
    #act
    interactor.create_share_ride(
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

    #assert
    storage.create_share_ride.assert_called_once_with(source=source,
            destination=destination ,
            is_flexible=is_flexible,
            datetime=datetime,
            from_datetime=from_datetime,
            to_datetime=to_datetime,
            no_of_seats_available=no_of_seats_available,
            assets_quantity=assets_quantity,
            user_id=user_id)
