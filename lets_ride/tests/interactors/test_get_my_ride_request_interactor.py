import pytest
from mock import create_autospec
from lets_ride.interactors.get_my_ride_requests_interactor \
    import GetMyRideRequestsInteractor
from lets_ride.interactors.storages.dtos \
    import UserDto, RideRequestDto
from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
   import PresenterInterface

def test_get_ride_requests_returns_ride_requets_list_requested_by_user(
    user_dto,
    post_dto,
    
    ):
    
    
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyRideRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
        
    