import pytest

from lets_ride.interactors.storages.dtos \
    import UserDto, RideRequestDto
from lets_ride.storages.storage_implementation \
    import StorageImplementation

@pytest.mark.django_db
def test_get_ride_requests_returns_ride_requets_list_requested_by_user(
    create_users,create_ride_requests,ride_request_dtos
    ):
    #Arrange
    user_id=1
    limit=10
    offset=1
    expected_output = ride_request_dtos
    print("ride_request_dtos:*****************",ride_request_dtos)
    storage = StorageImplementation()
    
    #Act
    response = storage.get_my_ride_requests_dto(user_id=user_id,
                                                limit=limit,
                                                offset=offset)
                                                
    print("response:*****************",response)
    #Assert
    assert response == expected_output

@pytest.mark.django_db
def test_get_ride_requests_when_no_requests_found():
    #Arrange
    user_id=1
    limit=10
    offset=1
    expected_output = []
    storage = StorageImplementation()
    
    #Act
    response = storage.get_my_ride_requests_dto(user_id=user_id,
                                                limit=limit,
                                                offset=offset)
                                                
    print("response:*****************",response)
    #Assert
    assert response == expected_output
