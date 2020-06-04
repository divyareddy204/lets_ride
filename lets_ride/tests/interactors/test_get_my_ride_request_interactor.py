import pytest
from mock import create_autospec, patch
from django_swagger_utils.drf_server.exceptions import BadRequest
from lets_ride.interactors.get_my_ride_requests_interactor \
    import GetMyRideRequestsInteractor
from lets_ride.interactors.storages.dtos \
    import RideRequestDto
from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
   import PresenterInterface
import datetime
from lets_ride.constants.enums import StatusValue

@pytest.fixture()
def ride_request_dtos():
    riderequestdtos = [
        RideRequestDto(
            user_id= 1,
            source= "hyderabad",
            destination= "bangloor",
            is_flexible= False,
            from_datetime= "",
            to_datetime= "",
            datetime= "",
            no_of_seats= 2,
            luggage_quantity= 2,
            accepted_person_id= 1,
            ),
        RideRequestDto(
            user_id= 1,
            source= "Mumbai",
            destination="Delhi",
            is_flexible= False,
            from_datetime= "",
            to_datetime= "",
            datetime= "2020-03-05 06:00:00.000000",
            no_of_seats= 3,
            luggage_quantity= 2,
            accepted_person_id= None
        )
        ]
    return riderequestdtos

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
    interactor = GetMyRideRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    presenter.raise_exception_for_invalid_limit.side_effect = BadRequest
    #Act
    with pytest.raises(BadRequest):
        interactor.get_my_ride_requests(
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
    interactor = GetMyRideRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    presenter.raise_exception_for_invalid_offset.side_effect = BadRequest
    #Act
    with pytest.raises(BadRequest):
        interactor.get_my_ride_requests(
            user_id=user_id,
            offset=offset,
            limit=limit,
            status=status,
            order_by=order_by,
            sort_by=sort_by
            )
    
    #Assert
    presenter.raise_exception_for_invalid_offset.assert_called_once_with()

@patch.object(GetMyRideRequestsInteractor, "_get_ride_request_with_status",
              return_value=ride_request_dtos)
def test_get_ride_requests_filter_by_status_value_expired_returns_ride_requests_details(
    user_dtos,ride_request_dtos,ride_request_response, my_ride_request_dto,
    ride_request_dto1,ride_request_dto2, ride_request_with_status_dtos
    ):
    
    #Arrange
    print(ride_request_with_status_dtos)
    user_id=2
    limit=2
    offset=0
    order_by="DESC"
    asc_order=False
    total_requests=2
    sort_by = datetime.datetime(2020,3,23,8,0,0)
    status=StatusValue.Expired.value
    expected_output = ride_request_response
    
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyRideRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    
    interactor._get_ride_request_with_status.return_value = my_ride_request_dto
    storage.get_total_ride_requests.return_value=2
    storage.get_accepted_persons_dtos.return_value=user_dtos
    storage.get_my_ride_requests_dto_filter_by_expired_status_value\
        .return_value=ride_request_dtos

    presenter.get_my_ride_requests_response.return_value=expected_output
    details=interactor._get_ride_request_with_status(ride_request_dtos)
    my_ride_request_dto=interactor._get_all_ride_request_details(
        total_requests=total_requests,
        limit=limit,
        offset=offset,
        list_of_ride_requests=details)

    #Act
    response = interactor.get_my_ride_requests(
        user_id=user_id,
        offset=offset,
        limit=limit,
        status=status,
        order_by=order_by,
        sort_by=sort_by
        )
    assert response == expected_output
    storage.get_my_ride_requests_dto_filter_by_expired_status_value\
    .assert_called_once_with(user_id=user_id,
                             limit=limit,
                             offset=offset,
                             asc_order=asc_order,
                             sort_by=sort_by)
    storage.get_total_ride_requests.assert_called_once_with(user_id=user_id)
    presenter.get_my_ride_requests_response.assert_called_once_with(
        user_dtos=user_dtos, my_ride_request_dto=my_ride_request_dto
        )

@patch.object(GetMyRideRequestsInteractor, "_get_ride_request_with_status",
              return_value=ride_request_dtos)

def test_get_ride_requests_order_by_ascending_returns_ride_request_sorted_by_datetime(
    user_dtos,ride_request_dtos,ride_request_response, my_ride_request_dto,
    ride_request_dto1,ride_request_dto2, ride_request_with_status_dtos
    ):
    #print(my_ride_request_dto)
    #print(ride_request_dtos)
    #Arrange
    print(ride_request_with_status_dtos)
    user_id=2
    limit=2
    offset=1
    total_requests=2
    sort_by = datetime.datetime(2020,3,23,8,0,0)
    status=None
    order_by ="ASC"
    asc_order = True
    expected_output = ride_request_response
    
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyRideRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    
    interactor._get_ride_request_with_status.return_value = my_ride_request_dto
    storage.get_total_ride_requests.return_value=2
    storage.get_accepted_persons_dtos.return_value=user_dtos
    storage.get_my_ride_requests_dto\
        .return_value=ride_request_dtos
    presenter.get_my_ride_requests_response.return_value=expected_output
    details=interactor._get_ride_request_with_status(ride_request_dtos)
    my_ride_request_dto=interactor._get_all_ride_request_details(
        total_requests=total_requests,
        limit=limit,
        offset=offset,
        list_of_ride_requests=details)
    #Act
    response = interactor.get_my_ride_requests(
        user_id=user_id,
        offset=offset,
        limit=limit,
        status=status,
        order_by=order_by,
        sort_by=sort_by
        )
    assert response == expected_output
    storage.get_my_ride_requests_dto\
    .assert_called_once_with(user_id=user_id,
                             limit=limit,
                             offset=offset,
                             sort_by=sort_by,
                             asc_order=asc_order)
    presenter.get_my_ride_requests_response.assert_called_once_with(
        user_dtos=user_dtos, my_ride_request_dto=my_ride_request_dto
        )

@patch.object(GetMyRideRequestsInteractor, "_get_ride_request_with_status",
              return_value=ride_request_dtos)
def test_get_ride_requests_order_by_descending_returns_ride_request_sorted_by_datetime(
    user_dtos,ride_request_dtos,ride_request_response, my_ride_request_dto,
    ride_request_dto1,ride_request_dto2, ride_request_with_status_dtos
    ):
    #print(my_ride_request_dto)
    #print(ride_request_dtos)
    #Arrange
    print(ride_request_with_status_dtos)
    user_id=2
    limit=2
    offset=1
    total_requests=2
    sort_by = datetime.datetime(2020,3,23,8,0,0)
    status=None
    order_by ="DESC"
    asc_order = False
    expected_output = ride_request_response
    
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyRideRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    
    interactor._get_ride_request_with_status.return_value = my_ride_request_dto
    storage.get_total_ride_requests.return_value=2
    storage.get_accepted_persons_dtos.return_value=user_dtos
    storage.get_my_ride_requests_dto\
        .return_value=ride_request_dtos
    presenter.get_my_ride_requests_response.return_value=expected_output
    details=interactor._get_ride_request_with_status(ride_request_dtos)
    my_ride_request_dto=interactor._get_all_ride_request_details(
        total_requests=total_requests,
        limit=limit,
        offset=offset,
        list_of_ride_requests=details)
    #Act
    response = interactor.get_my_ride_requests(
        user_id=user_id,
        offset=offset,
        limit=limit,
        status=status,
        order_by=order_by,
        sort_by=sort_by
        )
    assert response == expected_output
    storage.get_my_ride_requests_dto\
    .assert_called_once_with(user_id=user_id,
                             limit=limit,
                             offset=offset,
                             sort_by=sort_by,
                             asc_order=asc_order)
    presenter.get_my_ride_requests_response.assert_called_once_with(
        user_dtos=user_dtos, my_ride_request_dto=my_ride_request_dto
        )

@patch.object(GetMyRideRequestsInteractor, "_get_ride_request_with_status",
              return_value=ride_request_dtos)
def test_get_ride_requests_filter_by_status_value_Confirmed_returns_ride_requests_details(
    user_dtos,ride_request_dtos,ride_request_response, my_ride_request_dto,
    ride_request_dto1,ride_request_dto2, ride_request_with_status_dtos
    ):
    #print(my_ride_request_dto)
    #print(ride_request_dtos)
    #Arrange
    print(ride_request_with_status_dtos)
    user_id=2
    limit=2
    offset=1
    total_requests=2
    sort_by = "no_of_seats"
    status="Confirmed"
    order_by=None
    asc_order = False
    expected_output = ride_request_response
    
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyRideRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    
    interactor._get_ride_request_with_status.return_value = my_ride_request_dto
    storage.get_total_ride_requests.return_value=2
    storage.get_accepted_persons_dtos.return_value=user_dtos
    storage.get_my_ride_requests_dto_filter_by_confirmed_status_value\
        .return_value=ride_request_dtos
    presenter.get_my_ride_requests_response.return_value=expected_output
    details=interactor._get_ride_request_with_status(ride_request_dtos)
    my_ride_request_dto=interactor._get_all_ride_request_details(
        total_requests=total_requests,
        limit=limit,
        offset=offset,
        list_of_ride_requests=details)
    #Act
    response = interactor.get_my_ride_requests(
        user_id=user_id,
        offset=offset,
        limit=limit,
        status=status,
        order_by=order_by,
        sort_by=sort_by
        )
    assert response == expected_output
    storage.get_my_ride_requests_dto_filter_by_confirmed_status_value\
    .assert_called_once_with(user_id=user_id,
                             limit=limit,
                             offset=offset,
                             sort_by=sort_by,
                             asc_order=asc_order
                             )
    presenter.get_my_ride_requests_response.assert_called_once_with(
        user_dtos=user_dtos, my_ride_request_dto=my_ride_request_dto
        )

@patch.object(GetMyRideRequestsInteractor, "_get_ride_request_with_status",
              return_value=ride_request_dtos)
def test_get_ride_requests_filter_by_status_value_active_returns_ride_requests_details(
    user_dtos,ride_request_dtos,ride_request_response, my_ride_request_dto,
    ride_request_dto1,ride_request_dto2, ride_request_with_status_dtos
    ):
    #print(my_ride_request_dto)
    #print(ride_request_dtos)
    #Arrange
    print(ride_request_with_status_dtos)
    user_id=2
    limit=2
    offset=1
    total_requests=2
    sort_by = "datetime"
    status="Pending"
    order_by= "DESC"
    asc_order = False
    expected_output = ride_request_response
    
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyRideRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    
    interactor._get_ride_request_with_status.return_value = my_ride_request_dto
    storage.get_total_ride_requests.return_value=2
    storage.get_accepted_persons_dtos.return_value=user_dtos
    storage.get_my_ride_requests_dto_filter_by_active_status_value\
        .return_value=ride_request_dtos
    presenter.get_my_ride_requests_response.return_value=expected_output
    details=interactor._get_ride_request_with_status(ride_request_dtos)
    my_ride_request_dto=interactor._get_all_ride_request_details(
        total_requests=total_requests,
        limit=limit,
        offset=offset,
        list_of_ride_requests=details)
    #Act
    response = interactor.get_my_ride_requests(
        user_id=user_id,
        offset=offset,
        limit=limit,
        status=status,
        order_by=order_by,
        sort_by=sort_by
        )
    assert response == expected_output
    storage.get_my_ride_requests_dto_filter_by_active_status_value\
    .assert_called_once_with(user_id=user_id,
                             limit=limit,
                             offset=offset,
                             sort_by=sort_by,
                             asc_order=asc_order
                             )
    presenter.get_my_ride_requests_response.assert_called_once_with(
        user_dtos=user_dtos, my_ride_request_dto=my_ride_request_dto
        )

