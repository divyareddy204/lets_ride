import pytest
from mock import create_autospec, patch
from lets_ride.interactors.get_my_asset_request_interactor \
    import GetMyAssetRequestsInteractor
from lets_ride.interactors.storages.dtos \
    import UserDto, AssetRequestDto,AssetRequestWithStatusDto
from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
   import PresenterInterface
import datetime
from lets_ride.constants.enums \
        import StatusValue, AssetType, SensitivityType

@pytest.fixture()
def asset_request_dtos():
    assetrequestdtos = [
        AssetRequestDto(
            user_id= 1,
            source= "hyderabad",
            destination= "bangloor",
            flexible= True,
            from_datetime= "2020-09-04 06:00:00.00000",
            to_datetime= "2020-09-05 06:00:00.00000",
            datetime=None,
            no_of_assets= 2,
            asset_type = AssetType.parcel.value,
            sensitivity = SensitivityType.HighlySensitive.value,
            deliver_person = "ram",
            accepted_person_id= 1
            ),
        AssetRequestDto(
            user_id= 1,
            source= "Mumbai",
            destination= "delhi",
            flexible= False,
            from_datetime=None,
            to_datetime= None,
            datetime= "2020-09-05 06:00:00.00000",
            no_of_assets= 2,
            asset_type = AssetType.bags.value,
            sensitivity = SensitivityType.HighlySensitive.value,
            deliver_person = "ram",
            accepted_person_id= 2
            ),
        ]
    return assetrequestdtos

@patch.object(GetMyAssetRequestsInteractor, "_get_asset_request_with_status",
              return_value=asset_request_dtos)
def test_get_asset_requests_filter_by_status_value_expired_returns_asset_requests_details(
    user_dtos,asset_request_dtos,asset_request_response, my_asset_request_dto,
    asset_request_dto1,asset_request_dto2, asset_request_with_status_dtos
    ):
    #print(my_asset_request_dto)
    #print(asset_request_dtos)
    #Arrange
    print(asset_request_with_status_dtos)
    user_id=2
    limit=2
    offset=1
    total_requests=2
    sort_by = datetime.datetime(2020,3,23,8,0,0)
    status=StatusValue.Expired.value
    order ="ASC"
    expected_output = asset_request_response
    
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyAssetRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    
    interactor._get_asset_request_with_status.return_value = my_asset_request_dto
    storage.get_total_requests.return_value=2
    storage.get_accepted_persons_dtos.return_value=user_dtos
    storage.get_my_asset_requests_dto_filter_by_expired_status_value\
        .return_value=asset_request_dtos
    presenter.get_my_asset_requests_response.return_value=expected_output
    details=interactor._get_asset_request_with_status(asset_request_dtos)
    my_asset_request_dto=interactor._get_all_asset_request_details(
        total_requests=total_requests,
        limit=limit,
        offset=offset,
        list_of_asset_requests=details)
    #Act
    response = interactor.get_my_asset_requests(
        user_id=user_id,
        offset=offset,
        limit=limit,
        status=status,
        order=order,
        sort_by=sort_by
        )
    assert response == expected_output
    storage.get_my_asset_requests_dto_filter_by_expired_status_value\
    .assert_called_once_with(user_id=user_id,
                             limit=limit,
                             offset=offset)
    presenter.get_my_asset_requests_response.assert_called_once_with(
        user_dtos=user_dtos, my_asset_request_dto=my_asset_request_dto
        )

@patch.object(GetMyAssetRequestsInteractor, "_get_asset_request_with_status",
              return_value=asset_request_dtos)
def test_get_asset_requests_filter_by_status_value_Confirmed_returns_asset_requests_details(
    user_dtos,asset_request_dtos,asset_request_response, my_asset_request_dto,
    asset_request_dto1,asset_request_dto2, asset_request_with_status_dtos
    ):
    #print(my_asset_request_dto)
    #print(asset_request_dtos)
    #Arrange
    print(asset_request_with_status_dtos)
    user_id=2
    limit=2
    offset=1
    total_requests=2
    sort_by = None
    status="Confirmed"
    order=None
    expected_output = asset_request_response
    
    
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyAssetRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    
    interactor._get_asset_request_with_status.return_value = my_asset_request_dto
    storage.get_total_requests.return_value=2
    storage.get_accepted_persons_dtos.return_value=user_dtos
    storage.get_my_asset_requests_dto_filter_by_confirmed_status_value\
        .return_value=asset_request_dtos
    presenter.get_my_asset_requests_response.return_value=expected_output
    details=interactor._get_asset_request_with_status(asset_request_dtos)
    my_asset_request_dto=interactor._get_all_asset_request_details(
        total_requests=total_requests,
        limit=limit,
        offset=offset,
        list_of_asset_requests=details)
    #Act
    response = interactor.get_my_asset_requests(
        user_id=user_id,
        offset=offset,
        limit=limit,
        status=status,
        order=order,
        sort_by=sort_by
        )
    assert response == expected_output
    storage.get_my_asset_requests_dto_filter_by_confirmed_status_value\
    .assert_called_once_with(user_id=user_id,
                             limit=limit,
                             offset=offset)
    presenter.get_my_asset_requests_response.assert_called_once_with(
        user_dtos=user_dtos, my_asset_request_dto=my_asset_request_dto
        )

@patch.object(GetMyAssetRequestsInteractor, "_get_asset_request_with_status",
              return_value=asset_request_dtos)
def test_get_asset_requests_filter_by_status_value_active_returns_asset_requests_details(
    user_dtos,asset_request_dtos,asset_request_response, my_asset_request_dto,
    asset_request_dto1,asset_request_dto2, asset_request_with_status_dtos
    ):
    #print(my_asset_request_dto)
    #print(asset_request_dtos)
    #Arrange
    print(asset_request_with_status_dtos)
    user_id=2
    limit=2
    offset=1
    total_requests=2
    sort_by = None
    status="Pending"
    order=None
    expected_output = asset_request_response
    
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyAssetRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    
    interactor._get_asset_request_with_status.return_value = my_asset_request_dto
    storage.get_total_requests.return_value=2
    storage.get_accepted_persons_dtos.return_value=user_dtos
    storage.get_my_asset_requests_dto_filter_by_active_status_value\
        .return_value=asset_request_dtos
    presenter.get_my_asset_requests_response.return_value=expected_output
    details=interactor._get_asset_request_with_status(asset_request_dtos)
    my_asset_request_dto=interactor._get_all_asset_request_details(
        total_requests=total_requests,
        limit=limit,
        offset=offset,
        list_of_asset_requests=details)
    #Act
    response = interactor.get_my_asset_requests(
        user_id=user_id,
        offset=offset,
        limit=limit,
        status=status,
        order=order,
        sort_by=sort_by
        )
    assert response == expected_output
    storage.get_my_asset_requests_dto_filter_by_active_status_value\
    .assert_called_once_with(user_id=user_id,
                             limit=limit,
                             offset=offset)
    presenter.get_my_asset_requests_response.assert_called_once_with(
        user_dtos=user_dtos, my_asset_request_dto=my_asset_request_dto
        )

@patch.object(GetMyAssetRequestsInteractor, "_get_asset_request_with_status",
              return_value=asset_request_dtos)
def test_get_asset_requests_when_no_filtering_and_sorting_returns_asset_details(
    user_dtos,asset_request_dtos,asset_request_response, my_asset_request_dto,
    asset_request_dto1,asset_request_dto2, asset_request_with_status_dtos
    ):
    #print(my_asset_request_dto)
    #print(asset_request_dtos)
    #Arrange
    print(asset_request_with_status_dtos)
    user_id=2
    limit=2
    offset=1
    total_requests=2
    sort_by = None
    status=None
    order=None
    expected_output = asset_request_response
    
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyAssetRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    
    interactor._get_asset_request_with_status.return_value = my_asset_request_dto
    storage.get_total_requests.return_value=2
    storage.get_accepted_persons_dtos.return_value=user_dtos
    storage.get_my_asset_requests_dto\
        .return_value=asset_request_dtos
    presenter.get_my_asset_requests_response.return_value=expected_output
    details=interactor._get_asset_request_with_status(asset_request_dtos)
    my_asset_request_dto=interactor._get_all_asset_request_details(
        total_requests=total_requests,
        limit=limit,
        offset=offset,
        list_of_asset_requests=details)
    #Act
    response = interactor.get_my_asset_requests(
        user_id=user_id,
        offset=offset,
        limit=limit,
        status=status,
        order=order,
        sort_by=sort_by
        )
    assert response == expected_output
    storage.get_my_asset_requests_dto\
    .assert_called_once_with(user_id=user_id,
                             limit=limit,
                             offset=offset)
    presenter.get_my_asset_requests_response.assert_called_once_with(
        user_dtos=user_dtos, my_asset_request_dto=my_asset_request_dto
        )

"""@patch.object(GetMyAssetRequestsInteractor, "_get_asset_request_with_status",
              return_value=asset_request_dtos)

def test_get_asset_requests_order_by_ascending_returns_asset_request_sorted_by_datetime(
    user_dtos,asset_request_dtos,asset_request_response, my_asset_request_dto,
    asset_request_dto1,asset_request_dto2, asset_request_with_status_dtos
    ):
    #print(my_asset_request_dto)
    #print(asset_request_dtos)
    #Arrange
    print(asset_request_with_status_dtos)
    user_id=2
    limit=2
    offset=1
    total_requests=2
    sort_by = datetime.datetime(2020,3,23,8,0,0)
    status=None
    order ="ASC"
    expected_output = asset_request_response
    
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyAssetRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    
    interactor._get_asset_request_with_status.return_value = my_asset_request_dto
    storage.get_total_requests.return_value=2
    storage.get_accepted_persons_dtos.return_value=user_dtos
    storage.get_my_asset_requests_dto_sort_by_ascending_order\
        .return_value=asset_request_dtos
    presenter.get_my_asset_requests_response.return_value=expected_output
    details=interactor._get_asset_request_with_status(asset_request_dtos)
    my_asset_request_dto=interactor._get_all_asset_request_details(
        total_requests=total_requests,
        limit=limit,
        offset=offset,
        list_of_asset_requests=details)
    #Act
    response = interactor.get_my_asset_requests(
        user_id=user_id,
        offset=offset,
        limit=limit,
        status=status,
        order=order,
        sort_by=sort_by
        )
    assert response == expected_output
    storage.get_my_asset_requests_dto_sort_by_ascending_order\
    .assert_called_once_with(user_id=user_id,
                             limit=limit,
                             offset=offset,
                             sort_by=sort_by)
    presenter.get_my_asset_requests_response.assert_called_once_with(
        user_dtos=user_dtos, my_asset_request_dto=my_asset_request_dto
        )

@patch.object(GetMyAssetRequestsInteractor, "_get_asset_request_with_status",
              return_value=asset_request_dtos)
def test_get_asset_requests_order_by_decending_returns_asset_request_sorted_by_datetime(
    user_dtos,asset_request_dtos,asset_request_response, my_asset_request_dto,
    asset_request_dto1,asset_request_dto2, asset_request_with_status_dtos
    ):
    #print(my_asset_request_dto)
    #print(asset_request_dtos)
    #Arrange
    print(asset_request_with_status_dtos)
    user_id=2
    limit=2
    offset=1
    total_requests=2
    sort_by = datetime.datetime(2020,3,23,8,0,0)
    status=None
    order ="DESC"
    expected_output = asset_request_response
    
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyAssetRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    
    interactor._get_asset_request_with_status.return_value = my_asset_request_dto
    storage.get_total_requests.return_value=2
    storage.get_accepted_persons_dtos.return_value=user_dtos
    storage.get_my_asset_requests_dto_sort_by_descending_order\
        .return_value=asset_request_dtos
    presenter.get_my_asset_requests_response.return_value=expected_output
    details=interactor._get_asset_request_with_status(asset_request_dtos)
    my_asset_request_dto=interactor._get_all_asset_request_details(
        total_requests=total_requests,
        limit=limit,
        offset=offset,
        list_of_asset_requests=details)
    #Act
    response = interactor.get_my_asset_requests(
        user_id=user_id,
        offset=offset,
        limit=limit,
        status=status,
        order=order,
        sort_by=sort_by
        )
    assert response == expected_output
    storage.get_my_asset_requests_dto_sort_by_descending_order.\
    assert_called_once_with(user_id=user_id,
                             limit=limit,
                             offset=offset,
                             sort_by=sort_by)
    presenter.get_my_asset_requests_response.assert_called_once_with(
        user_dtos=user_dtos, my_asset_request_dto=my_asset_request_dto
        )
"""