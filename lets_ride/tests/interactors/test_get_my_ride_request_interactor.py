import pytest
from mock import create_autospec, patch
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
            flexible= False,
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
            flexible= False,
            from_datetime= "",
            to_datetime= "",
            datetime= "",
            no_of_seats= 2,
            luggage_quantity= 2,
            accepted_person_id= None
        )
        ]
    return riderequestdtos

@patch.object(GetMyRideRequestsInteractor, "_get_ride_request_with_status",
              return_value=ride_request_dtos)
def test_get_ride_requests_filter_by_status_value_expired_returns_ride_requests_details(
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
    status=StatusValue.Expired.value
    order ="ASC"
    expected_output = ride_request_response
    
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyRideRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    
    interactor._get_ride_request_with_status.return_value = my_ride_request_dto
    storage.get_total_requests.return_value=2
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
        order=order,
        sort_by=sort_by
        )
    assert response == expected_output
    storage.get_my_ride_requests_dto_filter_by_expired_status_value\
    .assert_called_once_with(user_id=user_id,
                             limit=limit,
                             offset=offset)
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
    order ="ASC"
    expected_output = ride_request_response
    
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyRideRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    
    interactor._get_ride_request_with_status.return_value = my_ride_request_dto
    storage.get_total_requests.return_value=2
    storage.get_accepted_persons_dtos.return_value=user_dtos
    storage.get_my_ride_requests_dto_sort_by_ascending_order\
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
        order=order,
        sort_by=sort_by
        )
    assert response == expected_output
    storage.get_my_ride_requests_dto_sort_by_ascending_order\
    .assert_called_once_with(user_id=user_id,
                             limit=limit,
                             offset=offset,
                             sort_by=sort_by)
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
    order ="DESC"
    expected_output = ride_request_response
    
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyRideRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    
    interactor._get_ride_request_with_status.return_value = my_ride_request_dto
    storage.get_total_requests.return_value=2
    storage.get_accepted_persons_dtos.return_value=user_dtos
    storage.get_my_ride_requests_dto_sort_by_descending_order\
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
        order=order,
        sort_by=sort_by
        )
    assert response == expected_output
    storage.get_my_ride_requests_dto_sort_by_descending_order\
    .assert_called_once_with(user_id=user_id,
                             limit=limit,
                             offset=offset,
                             sort_by=sort_by)
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
    sort_by = None
    status="Confirmed"
    order=None
    expected_output = ride_request_response
    
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyRideRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    
    interactor._get_ride_request_with_status.return_value = my_ride_request_dto
    storage.get_total_requests.return_value=2
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
        order=order,
        sort_by=sort_by
        )
    assert response == expected_output
    storage.get_my_ride_requests_dto_filter_by_confirmed_status_value\
    .assert_called_once_with(user_id=user_id,
                             limit=limit,
                             offset=offset)
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
    sort_by = None
    status="Pending"
    order=None
    expected_output = ride_request_response
    
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyRideRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    
    interactor._get_ride_request_with_status.return_value = my_ride_request_dto
    storage.get_total_requests.return_value=2
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
        order=order,
        sort_by=sort_by
        )
    assert response == expected_output
    storage.get_my_ride_requests_dto_filter_by_active_status_value\
    .assert_called_once_with(user_id=user_id,
                             limit=limit,
                             offset=offset)
    presenter.get_my_ride_requests_response.assert_called_once_with(
        user_dtos=user_dtos, my_ride_request_dto=my_ride_request_dto
        )

@patch.object(GetMyRideRequestsInteractor, "_get_ride_request_with_status",
              return_value=ride_request_dtos)
def test_get_ride_requests_when_no_filtering_and_sorting_returns_ride_details(
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
    sort_by = None
    status=None
    order=None
    expected_output = ride_request_response
    
    presenter = create_autospec(PresenterInterface)
    storage = create_autospec(PostStorageInterface)
    interactor = GetMyRideRequestsInteractor(
        presenter=presenter,
        storage=storage
        )
    
    interactor._get_ride_request_with_status.return_value = my_ride_request_dto
    storage.get_total_requests.return_value=2
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
        order=order,
        sort_by=sort_by
        )
    assert response == expected_output
    storage.get_my_ride_requests_dto\
    .assert_called_once_with(user_id=user_id,
                             limit=limit,
                             offset=offset)
    presenter.get_my_ride_requests_response.assert_called_once_with(
        user_dtos=user_dtos, my_ride_request_dto=my_ride_request_dto
        )
