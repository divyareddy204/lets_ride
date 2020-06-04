import pytest
from django_swagger_utils.drf_server.exceptions import BadRequest
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
            is_flexible= True,
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
            is_flexible= False,
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

def test_invalid_limit_value_returns_bad_request():
    #Arrange
    user_id = 2
    limit = -2
    offset = 0
    order_by = "ASC"
    status = StatusValue.Expired.value
    sort_by = datetime.datetime(2020,3,23,8,0,0)
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyAssetRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    presenter.raise_exception_for_invalid_limit.side_effect = BadRequest
    #Act
    with pytest.raises(BadRequest):
        interactor.get_my_asset_requests(
            user_id=user_id,
            offset=offset,
            limit=limit,
            status=status,
            order_by=order_by,
            sort_by=sort_by
            )
    
    #Assert
    presenter.raise_exception_for_invalid_limit.assert_called_once_with()

def test_invalid_offset_value_returns_bad_request():
    #Arrange
    user_id = 2
    limit = 2
    offset = -4
    order_by = "ASC"
    status = StatusValue.Expired.value
    sort_by = datetime.datetime(2020,3,23,8,0,0)
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyAssetRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    presenter.raise_exception_for_invalid_offset.side_effect = BadRequest
    #Act
    with pytest.raises(BadRequest):
        interactor.get_my_asset_requests(
            user_id=user_id,
            offset=offset,
            limit=limit,
            status=status,
            order_by=order_by,
            sort_by=sort_by
            )
    
    #Assert
    presenter.raise_exception_for_invalid_offset.assert_called_once_with()

@patch.object(GetMyAssetRequestsInteractor, "_get_asset_request_with_status",
              return_value=asset_request_dtos)
def test_get_asset_requests_filter_by_status_value_expired_returns_asset_requests_details(
    user_dtos,asset_request_dtos,asset_request_response, my_asset_request_dto,
    asset_request_dto1,asset_request_dto2, asset_request_with_status_dtos
    ):
    
    #Arrange
    print(asset_request_with_status_dtos)
    user_id=2
    limit=2
    offset=0
    order_by="DESC"
    asc_order=False
    total_requests=2
    sort_by = datetime.datetime(2020,3,23,8,0,0)
    status=StatusValue.Expired.value
    expected_output = asset_request_response
    
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyAssetRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    
    interactor._get_asset_request_with_status.return_value = my_asset_request_dto
    storage.get_total_asset_requests.return_value=2
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
        order_by=order_by,
        sort_by=sort_by
        )
    assert response == expected_output
    storage.get_my_asset_requests_dto_filter_by_expired_status_value\
    .assert_called_once_with(user_id=user_id,
                             limit=limit,
                             offset=offset,
                             asc_order=asc_order,
                             sort_by=sort_by)
    storage.get_total_asset_requests.assert_called_once_with(user_id=user_id)
    presenter.get_my_asset_requests_response.assert_called_once_with(
        user_dtos=user_dtos, my_asset_request_dto=my_asset_request_dto
        )

@patch.object(GetMyAssetRequestsInteractor, "_get_asset_request_with_status",
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
    order_by ="ASC"
    asc_order = True
    expected_output = asset_request_response
    
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyAssetRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    
    interactor._get_asset_request_with_status.return_value = my_asset_request_dto
    storage.get_total_asset_requests.return_value=2
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
        order_by=order_by,
        sort_by=sort_by
        )
    assert response == expected_output
    storage.get_my_asset_requests_dto\
    .assert_called_once_with(user_id=user_id,
                             limit=limit,
                             offset=offset,
                             sort_by=sort_by,
                             asc_order=asc_order)
    presenter.get_my_asset_requests_response.assert_called_once_with(
        user_dtos=user_dtos, my_asset_request_dto=my_asset_request_dto
        )

@patch.object(GetMyAssetRequestsInteractor, "_get_asset_request_with_status",
              return_value=asset_request_dtos)
def test_get_asset_requests_order_by_descending_returns_asset_request_sorted_by_datetime(
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
    order_by ="DESC"
    asc_order = False
    expected_output = asset_request_response
    
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyAssetRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    
    interactor._get_asset_request_with_status.return_value = my_asset_request_dto
    storage.get_total_asset_requests.return_value=2
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
        order_by=order_by,
        sort_by=sort_by
        )
    assert response == expected_output
    storage.get_my_asset_requests_dto\
    .assert_called_once_with(user_id=user_id,
                             limit=limit,
                             offset=offset,
                             sort_by=sort_by,
                             asc_order=asc_order)
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
    sort_by = "no_of_seats"
    status="Confirmed"
    order_by=None
    asc_order = False
    expected_output = asset_request_response
    
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyAssetRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    
    interactor._get_asset_request_with_status.return_value = my_asset_request_dto
    storage.get_total_asset_requests.return_value=2
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
        order_by=order_by,
        sort_by=sort_by
        )
    assert response == expected_output
    storage.get_my_asset_requests_dto_filter_by_confirmed_status_value\
    .assert_called_once_with(user_id=user_id,
                             limit=limit,
                             offset=offset,
                             sort_by=sort_by,
                             asc_order=asc_order
                             )
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
    sort_by = "datetime"
    status="Pending"
    order_by= "DESC"
    asc_order = False
    expected_output = asset_request_response
    
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyAssetRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    
    interactor._get_asset_request_with_status.return_value = my_asset_request_dto
    storage.get_total_asset_requests.return_value=2
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
        order_by=order_by,
        sort_by=sort_by
        )
    assert response == expected_output
    storage.get_my_asset_requests_dto_filter_by_active_status_value\
    .assert_called_once_with(user_id=user_id,
                             limit=limit,
                             offset=offset,
                             sort_by=sort_by,
                             asc_order=asc_order
                             )
    presenter.get_my_asset_requests_response.assert_called_once_with(
        user_dtos=user_dtos, my_asset_request_dto=my_asset_request_dto
        )
