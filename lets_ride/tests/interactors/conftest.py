import pytest
from lets_ride.models import User
from lets_ride.interactors.storages.dtos import UserDto, RideRequestDto

@pytest.fixture()
def user_dtos():
    userdtos = [
        UserDto(
            username= 'ram',
            mobile_number= "890235",
            password= "password"
            ),
        UserDto(
                username= 'shyam',
                mobile_number= "890234",
                password= "ram@123"
            )]
    return userdtos

pytest.fixture()
def ride_request_dtos():
    riderequestdtos = [
        RideRequestDto(
            user_id= 1,
            source= "hyderabad",
            destination= "bangloor",
            flexible= False,
            from_datetime= "",
            to_datetim= "",
            datetime= "",
            no_of_seats= 2,
            luggage_quantity= 2,
            accepted_person_id= 2,
    
            ),
        RideRequestDto(
            user_id= 1,
            source= "Mumbai",
            destination="Delhi",
            flexible= False,
            from_datetime= "",
            to_datetim= "",
            datetime= "",
            no_of_seats= 2,
            luggage_quantity= 2,
            accepted_person_id= 2
        )
        ]
pytest.fixture()
def ride_request_response():
    ride_request_response = {
  "total_no.of_requests": 0,
  "ride_requests": [
    {
      "source": "hyderabad",
      "destination": "bangloor",
      "from_datetime": "2020-09-04 06:00:00.000000-08:00",
      "fexible": True,
      "to_datetime": "2020-09-05 06:00:00.000000-08:00",
      "datetime": "",
      "no_of_seats": 2,
      "luggage_quantity": 1,
      "accepted_person": {
        "mobile_number": "890234",
        "user_name": "ram"
      },
      "status": "accepted"
    }
  ],
  "offset": 0,
  "limit": 0
}
    