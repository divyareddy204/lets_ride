import pytest
from lets_ride.models import User, RideRequest
from lets_ride.constants.enums import StatusValue
from datetime import datetime
from lets_ride.interactors.storages.dtos \
    import UserDto, RideRequestDto, RideRequestWithStatusDto, MyRideRequestsDto


@pytest.fixture()
def create_users():
    users = [
        {
            'username': 'ram',
            "mobile_number": "890235",
        },
        {
            'username': 'sham',
            "mobile_number": "890235",
        }
    ]
    for user in users:
        User.objects.create(
            username=user['username'],
            mobile_number=user["mobile_number"])


@pytest.fixture()
def create_ride_requests():
    riderequestdto ={
            "user_id": 1,
            "source": "Mumbai",
            "destination": "delhi",
            "flexible": False,
            "from_datetime":None,
            "to_datetime": None,
            "datetime": "2020-09-04 06:00:00.000000-08:00",
            "no_of_seats": 2,
            "luggage_quantity": 2,
            "accepted_person_id": 2,
            }
    RideRequest.objects.create(user_id=riderequestdto['user_id'],
        source = riderequestdto['source'],
        flexible =riderequestdto["flexible"],
        destination =riderequestdto["destination"],
        from_datetime=riderequestdto["from_datetime"],
        to_datetime=riderequestdto["to_datetime"],
        datetime=riderequestdto["datetime"],
        no_of_seats=riderequestdto["no_of_seats"],
        luggage_quantity=riderequestdto["luggage_quantity"],
        accepted_person_id=riderequestdto["accepted_person_id"]
        )
    
    riderequestdto={
            "user_id": 1,
            "source":"hyderabad",
            "destination": "bangloor",
            "flexible": True,
            "from_datetime": datetime(2020, 6, 22, 0, 0),
            "to_datetime":datetime(2020,6,23,0,0),
            "datetime": "",
            "no_of_seats": 2,
            "luggage_quantity": 2,
            "accepted_person_id": 2,
            }
    RideRequest.objects.create(
        user_id = riderequestdto['user_id'],
        source = riderequestdto['source'],
        flexible =riderequestdto["flexible"],
        destination =riderequestdto["destination"],
        from_datetime=riderequestdto["from_datetime"],
        to_datetime=riderequestdto["to_datetime"],
        datetime=riderequestdto["datetime"],
        no_of_seats=riderequestdto["no_of_seats"],
        luggage_quantity=riderequestdto["luggage_quantity"],
        accepted_person_id=riderequestdto["accepted_person_id"]
        )
@pytest.fixture()
def ride_request_dtos():
    riderequestdtos = [
        RideRequestDto(
            user_id= 1,
            source= "Mumbai",
            destination="Delhi",
            flexible= False,
            from_datetime= 'None',
            to_datetime= 'None',
            datetime= "2020-09-04 14:00:00+00:00",
            no_of_seats= 2,
            luggage_quantity= 2,
            accepted_person_id= 1
        ),
        RideRequestDto(
            user_id= 1,
            source= "hyderabad",
            destination= "bangloor",
            flexible= True,
            from_datetime= "2020-09-05 14:00:00+00:00",
            to_datetime= "2020-09-05 14:00:00+00:00",
            datetime= 'None',
            no_of_seats= 2,
            luggage_quantity= 2,
            accepted_person_id= 2,
            )
        ]
    return riderequestdtos