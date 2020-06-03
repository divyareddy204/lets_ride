import pytest
from lets_ride.models import User
from lets_ride.constants.enums import StatusValue, AssetType, SensitivityType
import datetime
from lets_ride.interactors.storages.dtos \
    import UserDto, RideRequestDto, RideRequestWithStatusDto, \
    MyRideRequestsDto, AssetRequestDto, AssetRequestWithStatusDto,\
    MyAssetRequestsDto, RideShareDto
@pytest.fixture()
def user_dtos():
    userdtos = [
        UserDto(
            user_id= 1,
            user_name= 'ram',
            mobile_number= "890235",
            ),
        UserDto(
            user_id= 2,
            user_name= 'shyam',
            mobile_number= "890234",
            )]
    return userdtos

@pytest.fixture()
def ride_request_dto1():
    riderequestdto = [
        RideRequestDto(
            user_id= 1,
            source= "hyderabad",
            destination= "bangloor",
            flexible= True,
            from_datetime= "2020-09-04 06:00:00.000000",
            to_datetime= "2020-09-05 06:00:00.000000",
            datetime= "",
            no_of_seats= 2,
            luggage_quantity= 2,
            accepted_person_id= 1,
            ),
        ]
    return riderequestdto


@pytest.fixture()
def ride_request_dto2():
    riderequestdto = [
        RideRequestDto(
            user_id= 1,
            source= "Mumbai",
            destination= "delhi",
            flexible= False,
            from_datetime=None,
            to_datetime= None,
            datetime= "2020-09-05 06:00:00",
            no_of_seats= 2,
            luggage_quantity= 2,
            accepted_person_id= 2,
            ),
        ]
    return riderequestdto

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
@pytest.fixture()
def ride_request_with_status_dtos():
    ride_request_with_status_dtos = [
        RideRequestWithStatusDto(
            ride_request_dto = ride_request_dto1,
            status=StatusValue.Confirmed.value
        ),
        RideRequestWithStatusDto(
            ride_request_dto = ride_request_dto2,
            status=StatusValue.Pending.value
            )
    ]
    return ride_request_with_status_dtos

@pytest.fixture()
def ride_request_with_status_dto1():
    ride_request_with_status_dtos = [
        RideRequestWithStatusDto(
            ride_request_dto = ride_request_dto1,
            status=StatusValue.Pending.value
        ),
    ]
    return ride_request_with_status_dtos


@pytest.fixture()
def my_ride_request_dto():
    my_ride_request_dto = MyRideRequestsDto(
        total_requests=2,
        request_dtos=ride_request_with_status_dtos,
        limit=2,
        offset=1
      )
    return my_ride_request_dto

@pytest.fixture()
def my_ride_request_dto1():
    my_ride_request_dto = MyRideRequestsDto(
        total_requests=1,
        request_dtos=ride_request_with_status_dtos,
        limit=2,
        offset=1
      )
    return my_ride_request_dto


@pytest.fixture()
def ride_request_response():
    ride_request_response = {
      "total_no.of_requests": 2,
      "ride_requests": [
        {
          "source": "hyderabad",
          "destination": "bangloor",
          "from_datetime": None,
          "fexible": False,
          "to_datetime": None,
          "datetime": "2020-09-05 06:00:00.000000",
          "no_of_seats": 2,
          "luggage_quantity": 1,
          "accepted_person": {},
          "status": "Pending"
        },
        {
          "source": "mumbai",
          "destination": "delhi",
          "from_datetime": "2020-09-04 06:00:00.000000",
          "fexible": True,
          "to_datetime": "2020-09-05 06:00:00.000000",
          "datetime": "",
          "no_of_seats": 2,
          "luggage_quantity": 1,
          "accepted_person": {
            "mobile_number": "890234",
            "user_name": "ram"
          },
          "status": "Confirmed"
        }

      ],
      "offset": 1,
      "limit": 2
    }
    return ride_request_response

@pytest.fixture()
def asset_request_dto1():
    assetrequestdto = [
        AssetRequestDto(
            user_id= 1,
            source= "hyderabad",
            destination= "bangloor",
            flexible= True,
            from_datetime= "2020-09-04 06:00:00.000000",
            to_datetime= "2020-09-05 06:00:00.000000",
            datetime= "",
            no_of_assets= 2,
            asset_type = AssetType.parcel.value,
            sensitivity = SensitivityType.HighlySensitive.value,
            deliver_person = "ram",
            accepted_person_id= 1,
            ),
        ]
    return assetrequestdto

@pytest.fixture()
def matched_ride_request_dto():
    ride_request_dto=[RideRequestDto(
            user_id=3,
            source='hyderabad',
            destination='kurnool',
            flexible=False,
            from_datetime='None', 
            to_datetime='None',
            datetime='2020-08-02 16:22:48.548978+00:00',
            no_of_seats=2,
            luggage_quantity=5,
            accepted_person_id=None)]
    return ride_request_dto

@pytest.fixture()
def matched_ride_request_response():
    matched_ride_requests ={
        'total_requests': 81,
        'requests': [
            {
            'source': 'hyderabad', 
            'user_id': 3,
            'destination': 'bangloor',
            'flexible': True,
            'datetime': 'None',
            'from_datetime': '2020-09-04 14:00:00',
            'to_datetime': '2020-09-04 14:00:00', 
            'no_of_seats': 2,
            'luggage_quantity': 2,
            'accepted_person': {},
            'status': 'Pending'}, 
            {'source': 'hyderabad',
            'user_id': 3,
            'destination': 'bangloor',
            'flexible': True, 'datetime': 'None',
            'from_datetime': '2020-09-04 14:00:00', 
            'to_datetime': '2020-09-04 14:00:00',
            'no_of_seats': 2,
            'luggage_quantity': 2,
            'accepted_person': {},
            'status': 'Pending'}], 
            'limit': 3, 'offset': 1}
    return matched_ride_requests


@pytest.fixture()
def ride_request_response1():
    ride_request_response = {
      "total_no.of_requests": 2,
      "ride_requests": [
        {
          "source": "hyderabad",
          "destination": "bangloor",
          "from_datetime": None,
          "fexible": False,
          "to_datetime": None,
          "datetime": "2020-09-05 06:00:00.000000",
          "no_of_seats": 2,
          "luggage_quantity": 1,
          "accepted_person": {},
          "status": "Pending"
        }],
        "offset": 1,
        "limit": 2
    }
    return ride_request_response

@pytest.fixture()
def asset_request_dto2():
    assetrequestdto = [
        AssetRequestDto(
            user_id= 1,
            source= "Mumbai",
            destination= "delhi",
            flexible= False,
            from_datetime=None,
            to_datetime= None,
            datetime= "2020-09-05 06:00:00",
            no_of_assets= 2,
            asset_type = AssetType.bags.value,
            sensitivity = SensitivityType.HighlySensitive.value,
            deliver_person = "ram",
            accepted_person_id= 2,
            ),
        ]
    return assetrequestdto
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

@pytest.fixture()
def ride_share_dtos():
    ride_share_dtos=[
        RideShareDto(
            user_id=3,
            source='mimbai',
            destination='chennai',
            flexible=False,
            from_datetime=None,
            to_datetime=None,
            datetime='2020, 7, 2, 21, 52, 48, 548978',
            no_of_seats_available=3,
            assets_quantity=2),
            RideShareDto(user_id=3,
            source='hyderabad',
            destination='kurnool',
            flexible=False,
            from_datetime=None,
            to_datetime=None,
            datetime='2020, 8, 2, 21, 52, 48, 548978',
            no_of_seats_available=2, assets_quantity=5),
            RideShareDto(user_id=3, source='hyderabad',
            destination='bangloor',
            flexible=False, from_datetime=None,
            to_datetime=None,
            datetime='2020, 8, 2, 16, 22, 48, 548978',
            no_of_seats_available=2, assets_quantity=5),
            RideShareDto(user_id=3, source='hyderabad',
            destination='kurnool',
            flexible=False, from_datetime=None,
            to_datetime=None,
            datetime='2020, 8, 2, 16, 22, 48, 548978',
            no_of_seats_available=2, assets_quantity=5)]
    return ride_share_dtos
    
@pytest.fixture()
def asset_request_with_status_dtos():
    asset_request_with_status_dtos = [
        AssetRequestWithStatusDto(
            asset_request_dto = asset_request_dto1,
            status=StatusValue.Confirmed.value
        ),
        AssetRequestWithStatusDto(
            asset_request_dto = asset_request_dto2,
            status=StatusValue.Pending.value
            )
    ]
    return asset_request_with_status_dtos

@pytest.fixture()
def my_asset_request_dto():
    my_asset_request_dto = MyAssetRequestsDto(
        total_requests=2,
        request_dtos=asset_request_with_status_dtos,
        limit=2,
        offset=1
      )
    return my_asset_request_dto

@pytest.fixture()
def asset_request_response():
    asset_request_response = {
      "total_no.of_requests": 2,
      "ride_requests": [
        {
          "source": "hyderabad",
          "destination": "bangloor",
          "from_datetime": None,
          "fexible": False,
          "to_datetime": None,
          "datetime": "2020-09-05 06:00:00.000000-08:00",
          "no_of_assets": 2,
          "asset_type": AssetType.parcel.value,
          "delever_person": "ram",
          "sensitivity":SensitivityType.HighlySensitive.value,
          "accepted_person": {},
          "status": "Pending"
        },
        {
          "source": "mumbai",
          "destination": "delhi",
          "from_datetime": "2020-09-04 06:00:00.000000-08:00",
          "fexible": True,
          "to_datetime": "2020-09-05 06:00:00.000000-08:00",
          "datetime": "",
          "no_of_assets": 2,
          "asset_type": AssetType.bags.value,
          "delever_person": "ram",
          "sensitivity":SensitivityType.HighlySensitive.value,
          "accepted_person": {
            "user_name": "ram",
            "mobile_number": "890234"
          },
          "status": "Confirmed"
        }

      ],
      "offset": 1,
      "limit": 2
    }
    return asset_request_response
