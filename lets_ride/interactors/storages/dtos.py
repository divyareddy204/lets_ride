from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass()
class UserDto:
    user_id: int
    user_name: str
    mobile_number: str

@dataclass()
class RideRequestDto:
    user_id: int
    source: str
    destination: str
    is_flexible: bool
    from_datetime: datetime
    to_datetime: datetime
    datetime: datetime
    no_of_seats: int
    luggage_quantity: int
    accepted_person_id: Optional[int]

@dataclass()
class RideShareDto:
    user_id: int
    source: str
    destination: str
    is_flexible: bool
    from_datetime: datetime
    to_datetime: datetime
    datetime: datetime
    no_of_seats_available: int
    assets_quantity: int

@dataclass()
class ShareTravelInfoDto:
    user_id: int
    source: str
    destination: str
    is_flexible: bool
    from_datetime: datetime
    to_datetime: datetime
    datetime: datetime
    medium: str
    assets_quantity: int

@dataclass()
class RideRequestWithStatusDto:
    ride_request_dto: RideRequestDto
    status: str

@dataclass()
class MyRideRequestsDto:
    total_requests: int
    request_dtos: [RideRequestWithStatusDto]
    limit: int
    offset: int

@dataclass()
class AssetRequestDto:
    user_id: int
    source: str
    destination: str
    is_flexible: bool
    from_datetime: datetime
    to_datetime: datetime
    datetime: datetime
    no_of_assets: int
    asset_type: str
    sensitivity: str
    deliver_person: str
    accepted_person_id: Optional[int]

@dataclass()
class AssetRequestWithStatusDto:
    asset_request_dto: AssetRequestDto
    status: str

@dataclass()
class MyAssetRequestsDto:
    total_requests: int
    request_dtos: [AssetRequestWithStatusDto]
    limit: int
    offset: int

@dataclass()
class MatchingRideRequestsDto:
    matchig_requests: [RideRequestDto]
    request_type: str

@dataclass()
class UserAccessDto:
    user_id: int
    access_token: str
    refresh_token: str
    expires_in: datetime