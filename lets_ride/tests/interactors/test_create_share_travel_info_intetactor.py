import pytest
from unittest.mock import create_autospec
from lets_ride.interactors.create_share_travel_info_interactor \
    import CreateShareTravelInfoInteractor
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.constants.enums import MediumType

def test_share_travel_info_creates_share_travel_info_object():
    
    
    source = "hyderabad"
    destination = "bangloor"
    flexible= True
    datetime= ""
    from_datetime = "2020,5,28,20,00,00"
    to_datetime = "2020,5,29,09,00,00"
    assets_quantity=2
    medium = MediumType.Bus.value
    user_id =1

    storage = create_autospec(PostStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateShareTravelInfoInteractor(
        storage = storage,
        presenter = presenter
        )
    #act
    interactor.create_share_travel_info(
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

    #assert
    storage.create_share_travel_info.assert_called_once_with(source=source,
            destination=destination ,
            flexible=flexible,
            datetime=datetime,
            from_datetime=from_datetime,
            to_datetime=to_datetime,
            medium=medium,
            assets_quantity=assets_quantity,
            user_id=user_id)
