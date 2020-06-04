import pytest
from datetime import datetime
from lets_ride.models import User, RideRequest, AssetTransportRequest
from lets_ride.constants.enums import StatusValue, AssetType, SensitivityType
from lets_ride.interactors.storages.dtos \
    import UserDto, RideRequestDto, RideRequestWithStatusDto, \
    MyRideRequestsDto, MyAssetRequestsDto, AssetRequestDto, \
    AssetRequestWithStatusDto, UserAccessDto

@pytest.fixture()
def user_access_dto():
    user_access_dto= UserAccessDto(
        user_id = 3,
        access_token = 'mbnZBmyNDz7KIRnTjQ3QBvnLAN7BTj',
        refresh_token= 'qHCVVNwdm8OWw2nDH9XbsPyhI5lIQQ',
        expires_in= '2052-02-10 20:56:09.642688'
        )
    return user_access_dto

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
def create_ride_requests():
    list_of_ride_requests =[ 
            {
            "user_id": 1,
            "source": "Mumbai",
            "destination": "delhi",
            "is_flexible": False,
            "from_datetime":None,
            "to_datetime": None,
            "datetime": datetime(2020, 9, 5, 0, 3),
            "no_of_seats": 2,
            "luggage_quantity": 2,
            "accepted_person_id": 2,
            },
             {
            "user_id": 1,
            "source":"hyderabad",
            "destination": "bangloor",
            "is_flexible": True,
            "from_datetime": datetime(2020, 9, 4, 0, 3),
            "to_datetime": datetime(2020, 9, 5, 0, 3),
            "datetime": "",
            "no_of_seats": 2,
            "luggage_quantity": 2,
            "accepted_person_id": 2,
            }],
    for riderequestdto in list_of_ride_requests:
        RideRequest.objects.create(
            user_id = riderequestdto[0]["user_id"],
            source = riderequestdto[0]["source"],
            is_flexible =riderequestdto[0]["is_flexible"],
            destination =riderequestdto[0]["destination"],
            from_datetime=riderequestdto[0]["from_datetime"],
            to_datetime=riderequestdto[0]["to_datetime"],
            no_of_seats=riderequestdto[0]["no_of_seats"],
            luggage_quantity=riderequestdto[0]["luggage_quantity"],
            accepted_person_id=riderequestdto[0]["accepted_person_id"]
            )

@pytest.fixture()
def create_ride_requests_with_accepted_person_none():
    list_of_ride_requests =[ 
            {
            "user_id": 1,
            "source": "Mumbai",
            "destination": "delhi",
            "is_flexible": False,
            "from_datetime":None,
            "to_datetime": None,
            "datetime": datetime(2020, 9, 5, 0, 3),
            "no_of_seats": 2,
            "luggage_quantity": 2,
            "accepted_person_id": None,
            },
             {
            "user_id": 1,
            "source":"hyderabad",
            "destination": "bangloor",
            "is_flexible": True,
            "from_datetime": datetime(2020, 9, 4, 0, 3),
            "to_datetime": datetime(2020, 9, 5, 0, 3),
            "datetime": "",
            "no_of_seats": 2,
            "luggage_quantity": 2,
            "accepted_person_id": 2,
            }],
    for riderequestdto in list_of_ride_requests:
        RideRequest.objects.create(
            user_id = riderequestdto[0]["user_id"],
            source = riderequestdto[0]["source"],
            is_flexible =riderequestdto[0]["is_flexible"],
            destination =riderequestdto[0]["destination"],
            from_datetime=riderequestdto[0]["from_datetime"],
            to_datetime=riderequestdto[0]["to_datetime"],
            no_of_seats=riderequestdto[0]["no_of_seats"],
            luggage_quantity=riderequestdto[0]["luggage_quantity"],
            accepted_person_id=riderequestdto[0]["accepted_person_id"]
            )

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
            accepted_person_id= 2,
            ),
        RideRequestDto(
            user_id= 1,
            source= "Mumbai",
            destination="Delhi",
            is_flexible= False,
            from_datetime= "",
            to_datetime= "",
            datetime= "",
            no_of_seats= 2,
            luggage_quantity= 2,
            accepted_person_id= 1
        )
        ]
    return riderequestdtos

@pytest.fixture()
def ride_request_dto1():
    riderequestdto =RideRequestDto(
            user_id= 1,
            source= "hyderabad",
            destination= "bangloor",
            is_flexible= True,
            from_datetime= datetime(2020, 9, 4, 0, 3),
            to_datetime= datetime(2020, 9, 5, 0, 3),
            datetime= "",
            no_of_seats= 2,
            luggage_quantity= 2,
            accepted_person_id= 2,
            )
    return riderequestdto

@pytest.fixture()
def ride_request_dto1_with_accepted_person_none():
    riderequestdto =RideRequestDto(
            user_id= 1,
            source= "hyderabad",
            destination= "bangloor",
            is_flexible= True,
            from_datetime= datetime(2020, 9, 4, 0, 3),
            to_datetime= datetime(2020, 9, 5, 0, 3),
            datetime= "",
            no_of_seats= 2,
            luggage_quantity= 2,
            accepted_person_id= None,
            )
    return riderequestdto

@pytest.fixture()
def ride_request_dto2():
    riderequestdto = RideRequestDto(
            user_id= 1,
            source= "Mumbai",
            destination= "delhi",
            is_flexible= False,
            from_datetime=None,
            to_datetime= None,
            datetime= datetime(2020, 9, 4, 0, 3),
            no_of_seats= 2,
            luggage_quantity= 2,
            accepted_person_id= 2,
            )
    return riderequestdto

@pytest.fixture()
def my_ride_request_dto(ride_request_dto1,ride_request_dto2):
    my_ride_request_dto=MyRideRequestsDto(
        total_requests=2,
        request_dtos=[
            RideRequestWithStatusDto(
                ride_request_dto=ride_request_dto1,
                status=StatusValue.Confirmed.value),
                RideRequestWithStatusDto(
                ride_request_dto=ride_request_dto2,
                status= StatusValue.Confirmed.value
                )],
        limit=2,
        offset=1
        )
    return my_ride_request_dto

@pytest.fixture()
def my_ride_request_dto_with_accepted_person_none(ride_request_dto1_with_accepted_person_none,
                            ride_request_dto2):
    my_ride_request_dto=MyRideRequestsDto(
        total_requests=2,
        request_dtos=[
            RideRequestWithStatusDto(
                ride_request_dto=ride_request_dto1_with_accepted_person_none,
                status=StatusValue.Confirmed.value),
                RideRequestWithStatusDto(
                ride_request_dto=ride_request_dto2,
                status= StatusValue.Confirmed.value
                )],
        limit=2,
        offset=1
        )
    return my_ride_request_dto
    

@pytest.fixture()
def ride_request_response():
    ride_request_response = {
      "total_requests": 2,
      "requests": [
        {
          "source": "hyderabad",
          "destination": "bangloor",
          "from_datetime": '2020-09-04 00:03:00',
          "is_flexible": True,
          "to_datetime": '2020-09-05 00:03:00',
          "datetime": '',
          "no_of_seats": 2,
          "luggage_quantity": 2,
          "accepted_person": {
                "user_name": "shyam",
                "mobile_number": "890234",
          },
          "status": "Confirmed",
          "user_id": 1
        },
        {
          "user_id":1,
          "source": "Mumbai",
          "destination": "delhi",
          "from_datetime":'None',
          "is_flexible": False,
          "to_datetime": 'None',
          "datetime": '2020-09-04 00:03:00',
          "no_of_seats": 2,
          "luggage_quantity": 2,
          "accepted_person": {
            "mobile_number": "890234",
            "user_name": "shyam"
          },
          "status": "Confirmed"
        }
        
      ],
      "offset": 1,
      "limit": 2
    }
    return ride_request_response

@pytest.fixture()
def ride_request_response_with_accepted_person_none():
    ride_request_response = {
      "total_requests": 2,
      "requests": [
        {
          "source": "hyderabad",
          "destination": "bangloor",
          "from_datetime": '2020-09-04 00:03:00',
          "is_flexible": True,
          "to_datetime": '2020-09-05 00:03:00',
          "datetime": '',
          "no_of_seats": 2,
          "luggage_quantity": 2,
          "accepted_person": {},
          "status": "Confirmed",
          "user_id": 1
        },
        {
          "user_id":1,
          "source": "Mumbai",
          "destination": "delhi",
          "from_datetime":'None',
          "is_flexible": False,
          "to_datetime": 'None',
          "datetime": '2020-09-04 00:03:00',
          "no_of_seats": 2,
          "luggage_quantity": 2,
          "accepted_person": {
            "mobile_number": "890234",
            "user_name": "shyam"
          },
          "status": "Confirmed"
        }
        
      ],
      "offset": 1,
      "limit": 2
    }
    return ride_request_response


@pytest.fixture()
def create_asset_requests():
    list_of_asset_requests =[ 
            {
            "user_id": 1,
            "source": "Mumbai",
            "destination": "delhi",
            "is_flexible": False,
            "from_datetime":None,
            "to_datetime": None,
            "datetime": datetime(2020, 9, 5, 0, 3),
            "no_of_assets": 2,
            "sensitivity": SensitivityType.HighlySensitive.value,
            "asset_type": AssetType.parcel.value,
            "deliver_person": "ram",
            "accepted_person_id": 2,
            },
             {
            "user_id": 1,
            "source":"hyderabad",
            "destination": "bangloor",
            "is_flexible": True,
            "from_datetime": datetime(2020, 9, 4, 0, 3),
            "to_datetime": datetime(2020, 9, 5, 0, 3),
            "datetime": "",
            "no_of_assets": 5,
            "sensitivity": SensitivityType.Sensitive.value,
            "asset_type": AssetType.bags.value,
            "deliver_person": "shayam",
            "accepted_person_id": 2,
            }],
    for assetrequestdto in list_of_asset_requests:
        AssetTransportRequest.objects.create(
            user_id = assetrequestdto[0]["user_id"],
            source = assetrequestdto[0]["source"],
            is_flexible =assetrequestdto[0]["is_flexible"],
            destination =assetrequestdto[0]["destination"],
            from_datetime=assetrequestdto[0]["from_datetime"],
            to_datetime=assetrequestdto[0]["to_datetime"],
            no_of_assets=assetrequestdto[0]["no_of_assets"],
            sensitivity=assetrequestdto[0]["sensitivity"],
            asset_type=assetrequestdto[0]["asset_type"],
            deliver_person=assetrequestdto[0]["deliver_person"],
            accepted_person_id=assetrequestdto[0]["accepted_person_id"]
            )


@pytest.fixture()
def asset_request_dto1():
    assetrequestdto =AssetRequestDto(
            user_id= 1,
            source= "hyderabad",
            destination= "bangloor",
            is_flexible= True,
            from_datetime= datetime(2020, 9, 4, 0, 3),
            to_datetime= datetime(2020, 9, 5, 0, 3),
            datetime= "",
            no_of_assets= 5,
            sensitivity= SensitivityType.Sensitive.value,
            asset_type= AssetType.bags.value,
            deliver_person= "shayam",
            accepted_person_id= 2,
            )
    return assetrequestdto

@pytest.fixture()
def asset_request_dto2():
    assetrequestdto = AssetRequestDto(
            user_id= 1,
            source= "Mumbai",
            destination= "delhi",
            is_flexible= False,
            from_datetime=None,
            to_datetime= None,
            datetime= datetime(2020, 9, 4, 0, 3),
            no_of_assets= 2,
            sensitivity= SensitivityType.Normal.value,
            asset_type= AssetType.parcel.value,
            deliver_person= "shyam",
            accepted_person_id= 2,
            )
    return assetrequestdto

@pytest.fixture()
def my_asset_request_dto(asset_request_dto1,asset_request_dto2):
    my_asset_request_dto=MyAssetRequestsDto(
        total_requests=2,
        request_dtos=[
            AssetRequestWithStatusDto(
                asset_request_dto=asset_request_dto1,
                status=StatusValue.Confirmed.value),
                AssetRequestWithStatusDto(
                asset_request_dto=asset_request_dto2,
                status= StatusValue.Confirmed.value
                )],
        limit=2,
        offset=1
        )
    return my_asset_request_dto

@pytest.fixture()
def my_asset_request_dto_with_no_assert_requests():
    my_asset_request_dto=MyAssetRequestsDto(
        total_requests=0,
        request_dtos=[
                ],
        limit=5,
        offset=2
        )
    return my_asset_request_dto

@pytest.fixture()
def my_ride_request_dto_with_no_ride_requests():
    my_ride_request_dto=MyRideRequestsDto(
        total_requests=0,
        request_dtos=[
                ],
        limit=2,
        offset=1
        )
    return my_ride_request_dto

@pytest.fixture()
def my_asset_request_dto_with_accepted_person_none(
    asset_request_dto1_with_accepted_person_none,
    asset_request_dto2):
    my_asset_request_dto=MyAssetRequestsDto(
        total_requests=2,
        request_dtos=[
            AssetRequestWithStatusDto(
                asset_request_dto=asset_request_dto1_with_accepted_person_none,
                status=StatusValue.Pending.value),
                AssetRequestWithStatusDto(
                asset_request_dto=asset_request_dto2,
                status= StatusValue.Confirmed.value
                )],
        limit=2,
        offset=1
        )
    return my_asset_request_dto

@pytest.fixture()
def asset_request_response_with_no_asset_requests():
    asset_request_response = {
        "total_requests": 0,
        "requests":[],
        "offset": 2,
        "limit": 5
    }
    return asset_request_response

@pytest.fixture()
def ride_request_response_with_no_ride_requests():
    ride_request_response = {
        "total_requests": 0,
        "requests":[],
        "offset": 1,
        "limit": 2
    }
    return ride_request_response


@pytest.fixture()
def asset_request_response():
    asset_request_response = {
      "total_requests": 2,
      "requests": [
        {
          "source": "hyderabad",
          "destination": "bangloor",
          "from_datetime": '2020-09-04 00:03:00',
          "is_flexible": True,
          "to_datetime": '2020-09-05 00:03:00',
          "datetime": '',
          "no_of_assets": 5,
          "sensitivity": SensitivityType.Sensitive.value,
          "asset_type": AssetType.bags.value,
          "deliver_person": "shayam",
          "accepted_person": {
                "user_name": "shyam",
                "mobile_number": "890234",
          },
          "status": "Confirmed",
          "user_id": 1
        },
        {
          "user_id":1,
          "source": "Mumbai",
          "destination": "delhi",
          "from_datetime":'None',
          "is_flexible": False,
          "to_datetime": 'None',
          "datetime": '2020-09-04 00:03:00',
          "no_of_assets": 2,
          "sensitivity": SensitivityType.Normal.value,
          "asset_type": AssetType.parcel.value,
          "deliver_person": "shyam",
          "accepted_person": {
              "user_name": "shyam",
              "mobile_number": "890234",
          },
          "status": "Confirmed"
        }
        
      ],
      "offset": 1,
      "limit": 2
    }
    return asset_request_response

@pytest.fixture()
def asset_request_dto1_with_accepted_person_none():
    assetrequestdto =AssetRequestDto(
            user_id= 1,
            source= "hyderabad",
            destination= "bangloor",
            is_flexible= True,
            from_datetime= datetime(2020, 9, 4, 0, 3),
            to_datetime= datetime(2020, 9, 5, 0, 3),
            datetime= "",
            no_of_assets= 5,
            sensitivity= SensitivityType.Sensitive.value,
            asset_type= AssetType.bags.value,
            deliver_person= "shayam",
            accepted_person_id= None,
            )
    return assetrequestdto

@pytest.fixture()
def asset_request_response_with_accepted_person_none():
    asset_request_response = {
      "total_requests": 2,
      "requests": [
        {
          "source": "hyderabad",
          "destination": "bangloor",
          "from_datetime": '2020-09-04 00:03:00',
          "is_flexible": True,
          "to_datetime": '2020-09-05 00:03:00',
          "datetime": '',
          "no_of_assets": 5,
          "sensitivity": SensitivityType.Sensitive.value,
          "asset_type": AssetType.bags.value,
          "deliver_person": "shayam",
          "accepted_person": {},
          "status": "Pending",
          "user_id": 1
        },
        {
          "user_id":1,
          "source": "Mumbai",
          "destination": "delhi",
          "from_datetime":'None',
          "is_flexible": False,
          "to_datetime": 'None',
          "datetime": '2020-09-04 00:03:00',
          "no_of_assets": 2,
          "sensitivity": SensitivityType.Normal.value,
          "asset_type": AssetType.parcel.value,
          "deliver_person": "shyam",
          "accepted_person": {
              "user_name": "shyam",
              "mobile_number": "890234",
          },
          "status": "Confirmed"
        }
        
      ],
      "offset": 1,
      "limit": 2
    }
    return asset_request_response