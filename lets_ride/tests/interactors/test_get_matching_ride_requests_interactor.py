import pytest
from mock import create_autospec, patch
from lets_ride.interactors.get_matching_ride_requests_interactor \
    import GetMatchingRideRequests
from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
   import PresenterInterface

def get_matching_ride_request_returns_list_of_user_dtos(
    ride_share_dtos, matched_ride_request_dto, matched_ride_request_response):

    #Arrange
    user_id = 3
    expected_output = matched_ride_request_response

    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMatchingRideRequests(
        presenter=presenter,
        storage=storage
        )
    storage.get_user_ride_shares_from_current_day.return_value = ride_share_dtos
    storage.get_matching_ride_requests_dto_without_flexible_timings.\
    return_value = matched_ride_request_response

    #Act
    response = interactor.get_matching_ride_requests(user_id=user_id)

    #Assert
    assert response == expected_output
    storage.get_user_ride_shares_from_current_day.\
    assert_called_once_with(user_id=user_id)
