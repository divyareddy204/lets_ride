import pytest

from lets_ride.interactors.storages.dtos \
    import UserDto, AssetRequestDto
from lets_ride.storages.storage_implementation \
    import StorageImplementation

@pytest.mark.django_db
def test_get_asset_requests_returns_asset_trasnsport_requets_list_requested_by_user(
    create_users,create_asset_requests,asset_request_dtos
    ):
    #Arrange
    user_id=1
    limit=3
    offset=0
    expected_output = asset_request_dtos
    storage = StorageImplementation()
    
    #Act
    response = storage.get_my_asset_requests_dto(user_id=user_id,
                                                limit=limit,
                                                offset=offset)

    #Assert
    print("response:",response)
    assert response == expected_output

@pytest.mark.django_db
def test_get_asset_requests_when_no_requests_found():
    #Arrange
    user_id=1
    limit=10
    offset=1
    expected_output = []
    storage = StorageImplementation()
    
    #Act
    response = storage.get_my_asset_requests_dto(user_id=user_id,
                                                limit=limit,
                                                offset=offset)
                                                
    print("response:*****************",response)
    #Assert
    assert response == expected_output
