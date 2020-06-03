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

@pytest.mark.django_db
def test_get_ride_requests_returns_ride_requets_list_requested_by_user(
    create_users,create_ride_requests,ride_request_response,ride_request_dto1,
    ride_request_dto2, my_ride_request_dto,user_dtos, ride_request_dtos, 
    ride_request_with_status_dtos
    ):
    #Arrange
    user_id=2
    limit=2
    offset=1
    total_requests =2
    list_of_accepted_persons_ids=[1,2]
    expected_output = ride_request_response
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyRideRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    details=interactor._get_ride_request_with_status(ride_request_dtos)
    my_ride_request_dto=interactor._get_all_ride_request_details(
        total_requests=total_requests,
        limit=limit,
        offset=offset,
        list_of_ride_requests=details)
    print(expected_output)
    storage.get_total_requests.return_value=2
    storage.get_accepted_persons_dtos.return_value=user_dtos
    storage.get_my_ride_requests_dto.return_value=ride_request_dtos
    presenter.get_my_ride_requests_response.return_value=expected_output
    #Act
    response = interactor.get_my_ride_requests(
        user_id=user_id,
        offset=offset,
        limit=limit
        )
    
    #Assert
    print(response)
    print("(*************************")
    assert response == expected_output
    storage.get_my_ride_requests_dto.assert_called_once_with(user_id=user_id,
                                                             limit=limit,
                                                             offset=offset)
    storage.get_accepted_persons_dtos.assert_called_once_with(
        list_of_accepted_persons_ids=list_of_accepted_persons_ids)
    presenter.get_my_ride_requests_response.assert_called_once_with(
        user_dtos=user_dtos, my_ride_request_dto=my_ride_request_dto
        )