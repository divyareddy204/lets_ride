import pytest
from mock import create_autospec, patch
from django_swagger_utils.drf_server.exceptions import BadRequest
from lets_ride.interactors.get_matching_ride_requests_interactor \
    import GetMatchingRideRequests
from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
   import PresenterInterface

def test_get_matching_ride_request_returns_list_of_user_dtos(
    ride_share_dtos, matched_ride_request_dto, matched_ride_request_response):

    #Arrange
    user_id = 3
    limit = -10
    offset = 0
    
    expected_output = matched_ride_request_response

    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMatchingRideRequests(
        presenter=presenter,
        storage=storage
        )
    presenter.raise_exception_for_invalid_limit.side_effect = BadRequest

    #Act
    with pytest.raises(BadRequest):
        interactor.get_matching_ride_requests(
            user_id=user_id,
            limit=limit,
            offset=offset)

    #Assert
    presenter.raise_exception_for_invalid_limit.\
    assert_called_once_with()
