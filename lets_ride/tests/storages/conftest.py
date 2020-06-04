import pytest
from lets_ride.models import User, RideRequest, AssetTransportRequest
from lets_ride.constants.enums import StatusValue, AssetType, SensitivityType
from datetime import datetime
from lets_ride.interactors.storages.dtos \
    import UserDto, RideRequestDto, RideRequestWithStatusDto, \
    MyRideRequestsDto, AssetRequestDto


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
            "source": "mumbai",
            "destination": "delhi",
            "is_flexible": False,
            "from_datetime":None,
            "to_datetime": None,
            "datetime": datetime(2020, 9, 3, 18, 33),
            "no_of_seats": 2,
            "luggage_quantity": 2,
            "accepted_person_id": 2,
            }
    RideRequest.objects.create(user_id=riderequestdto['user_id'],
        source = riderequestdto['source'],
        is_flexible =riderequestdto["is_flexible"],
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
            "is_flexible": True,
            "from_datetime": datetime(2020, 9, 3, 19, 0),
            "to_datetime":datetime(2020, 9, 4, 19, 0),
            "datetime": None,
            "no_of_seats": 2,
            "luggage_quantity": 2,
            "accepted_person_id": 2,
            }
    RideRequest.objects.create(
        user_id = riderequestdto['user_id'],
        source = riderequestdto['source'],
        is_flexible =riderequestdto["is_flexible"],
        destination =riderequestdto["destination"],
        from_datetime=riderequestdto["from_datetime"],
        to_datetime=riderequestdto["to_datetime"],
        datetime=riderequestdto["datetime"],
        no_of_seats=riderequestdto["no_of_seats"],
        luggage_quantity=riderequestdto["luggage_quantity"],
        accepted_person_id=riderequestdto["accepted_person_id"]
        )
@pytest.fixture()
def asset_request_dtos():
    assetrequestdtos = [
        AssetRequestDto(
            user_id= 1,
            source= "mumbai",
            destination="delhi",
            is_flexible= False,
            from_datetime= None,
            to_datetime= None,
            datetime= datetime(2020, 9, 3, 18, 33),
            no_of_assets= 2,
            asset_type = AssetType.bags.value,
            sensitivity = SensitivityType.HighlySensitive.value,
            deliver_person = "ram",
            accepted_person_id= 2
        ),
        AssetRequestDto(
            user_id= 1,
            source= "hyderabad",
            destination= "bangloor",
            is_flexible= True,
            from_datetime= datetime(2020, 9, 3, 19, 0),
            to_datetime= datetime(2020, 9, 4, 19, 0),
            datetime= None,
            no_of_assets= 2,
            asset_type = AssetType.parcel.value,
            sensitivity = SensitivityType.HighlySensitive.value,
            deliver_person = "ram",
            accepted_person_id= 2,
            )
        ]
    return assetrequestdtos
    
    
@pytest.fixture()
def create_asset_requests():
    assetrequestdto ={
            "user_id": 1,
            "source": "mumbai",
            "destination": "delhi",
            "is_flexible": False,
            "from_datetime":None,
            "to_datetime": None,
            "datetime": datetime(2020, 9, 4, 0, 3),
            "no_of_assets": 2,
            "asset_type": AssetType.bags.value,
            "sensitivity":SensitivityType.HighlySensitive.value,
            "deliver_person": "ram",
            "accepted_person_id": 2,
            }
    AssetTransportRequest.objects.create(user_id=assetrequestdto['user_id'],
        source = assetrequestdto['source'],
        is_flexible =assetrequestdto["is_flexible"],
        destination =assetrequestdto["destination"],
        from_datetime=assetrequestdto["from_datetime"],
        to_datetime=assetrequestdto["to_datetime"],
        datetime=assetrequestdto["datetime"],
        no_of_assets=assetrequestdto["no_of_assets"],
        sensitivity=assetrequestdto["sensitivity"],
        asset_type=assetrequestdto["asset_type"],
        deliver_person=assetrequestdto["deliver_person"],
        accepted_person_id=assetrequestdto["accepted_person_id"]
        )
    
    assetrequestdto={
            "user_id": 1,
            "source":"hyderabad",
            "destination": "bangloor",
            "is_flexible": True,
            "from_datetime": datetime(2020, 9, 4, 0, 30),
            "to_datetime": datetime(2020, 9, 5, 0, 30), 
            "datetime": None,
            "no_of_assets": 2,
            "asset_type" : AssetType.parcel.value,
            "sensitivity" : SensitivityType.HighlySensitive.value,
            "deliver_person" : "ram",
            "accepted_person_id": 2,
            }
    AssetTransportRequest.objects.create(user_id=assetrequestdto['user_id'],
        source = assetrequestdto['source'],
        is_flexible =assetrequestdto["is_flexible"],
        destination =assetrequestdto["destination"],
        from_datetime=assetrequestdto["from_datetime"],
        to_datetime=assetrequestdto["to_datetime"],
        datetime=assetrequestdto["datetime"],
        no_of_assets=assetrequestdto["no_of_assets"],
        sensitivity=assetrequestdto["sensitivity"],
        asset_type=assetrequestdto["asset_type"],
        deliver_person=assetrequestdto["deliver_person"],
        accepted_person_id=assetrequestdto["accepted_person_id"]
        )

@pytest.fixture()
def create_asset_request_with_no_accepted_id():
    assetrequestdto ={
            "user_id": 1,
            "source": "mumbai",
            "destination": "delhi",
            "is_flexible": False,
            "from_datetime":None,
            "to_datetime": None,
            "datetime": datetime(2020, 9, 4, 0, 3),
            "no_of_assets": 2,
            "asset_type": AssetType.bags.value,
            "sensitivity":SensitivityType.HighlySensitive.value,
            "deliver_person": "ram",
            "accepted_person_id": None,
            }
    AssetTransportRequest.objects.create(user_id=assetrequestdto['user_id'],
        source = assetrequestdto['source'],
        is_flexible =assetrequestdto["is_flexible"],
        destination =assetrequestdto["destination"],
        from_datetime=assetrequestdto["from_datetime"],
        to_datetime=assetrequestdto["to_datetime"],
        datetime=assetrequestdto["datetime"],
        no_of_assets=assetrequestdto["no_of_assets"],
        sensitivity=assetrequestdto["sensitivity"],
        asset_type=assetrequestdto["asset_type"],
        deliver_person=assetrequestdto["deliver_person"],
        accepted_person_id=assetrequestdto["accepted_person_id"]
        )

@pytest.fixture()
def create_ride_requests_with_no_accepted_id():
    riderequestdto ={
            "user_id": 1,
            "source": "mumbai",
            "destination": "delhi",
            "is_flexible": False,
            "from_datetime":None,
            "to_datetime": None,
            "datetime": datetime(2020, 9, 3, 18, 33),
            "no_of_seats": 2,
            "luggage_quantity": 2,
            "accepted_person_id": None,
            }
    RideRequest.objects.create(user_id=riderequestdto['user_id'],
        source = riderequestdto['source'],
        is_flexible =riderequestdto["is_flexible"],
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
            source= "hyderabad",
            destination= "bangloor",
            is_flexible= True,
            from_datetime= datetime(2020, 9, 3, 13, 30),
            to_datetime= datetime(2020, 9, 4, 13, 30),
            datetime= None,
            no_of_seats= 2,
            luggage_quantity= 2,
            accepted_person_id= 2,
            )
        ]
    return riderequestdtos

@pytest.fixture()
def ride_request_dto_with_accepted_person_none():
    riderequestdtos = [
        RideRequestDto(
            user_id= 1,
            source= "hyderabad",
            destination= "bangloor",
            is_flexible= True,
            from_datetime= datetime(2020, 9, 3, 13, 30),
            to_datetime= datetime(2020, 9, 4, 13, 30),
            datetime= None,
            no_of_seats= 2,
            luggage_quantity= 2,
            accepted_person_id= None,
            )
        ]
    return riderequestdtos

"""RideRequestDto(
            user_id= 1,
            source= "mumbai",
            destination="delhi",
            is_flexible= False,
            from_datetime= None,
            to_datetime= None,
            datetime= datetime(2020, 9, 3, 13, 3),
            no_of_seats= 2,
            luggage_quantity= 2,
            accepted_person_id= 2
        ),"""