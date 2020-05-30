from abc import ABC
from abc import abstractmethod
from typing import List
from .dtos import UserDto, RideRequestDto, AssetRequestDto
from lets_ride.constants.enums import AssetType, SensitivityType, MediumType

class PostStorageInterface(ABC):

    @abstractmethod
    def validate_password_for_user(self, user_name: str,
                                    password: str) ->int:
        pass

    @abstractmethod
    def validate_user_name(self, user_name: str):
        pass

    @abstractmethod
    def create_user(self, user_name: str, mobile_number: str, password: str):
        pass

    @abstractmethod
    def get_user_profile(self, user_name: str) ->UserDto:
        pass

    @abstractmethod
    def create_ride_request(self,
                            source: str,
                            destination: str,
                            flexible: bool,
                            datetime: str,
                            from_datetime: str,
                            to_datetime: str,
                            no_of_seats: int,
                            luggage_quantity: int,
                            user_id: int)->int:
        pass

    @abstractmethod
    def create_asset_transport_request(self,
                                    source: str,
                                    destination: str,
                                    flexible: bool,
                                    datetime: str,
                                    from_datetime: str,
                                    to_datetime: str,
                                    no_of_assets: int,
                                    asset_type: AssetType,
                                    sensitivity: SensitivityType,
                                    deliver_person: str,
                                    user_id: int):
            pass

    @abstractmethod
    def create_share_ride(self,
                          source: str,
                            destination: str,
                            flexible: bool,
                            datetime: str,
                            from_datetime: str,
                            to_datetime: str,
                            no_of_seats_available: int,
                            assets_quantity: int,
                            user_id: int):

        pass

    @abstractmethod
    def create_share_travel_info(self,
                                source: str,
                                destination: str,
                                flexible: bool,
                                datetime: str,
                                from_datetime: str,
                                to_datetime: str,
                                medium: MediumType,
                                assets_quantity: int,
                                user_id: int):
        pass

    @abstractmethod
    def get_my_ride_requests_dto(self, user_id: int)->List[RideRequestDto]:
        pass


    @abstractmethod
    def get_accepted_persons_dtos(
        self,
        list_of_accepted_persons_ids: List[int])->List[UserDto]:
        pass

    @abstractmethod
    def get_my_asset_requests_dto(
        self, user_id: int,
        limit: int, offset: int)->List[AssetRequestDto]:
        pass

    @abstractmethod
    def get_total_requests(self)->int:
        pass

    @abstractmethod
    def get_total_asset_requests(self)->int:
        pass