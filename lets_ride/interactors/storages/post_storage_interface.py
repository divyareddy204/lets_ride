from abc import ABC
from abc import abstractmethod
from typing import List
from .dtos import UserDto, RideRequestDto, AssetRequestDto, RideShareDto,\
    ShareTravelInfoDto
from datetime import datetime
from lets_ride.constants.enums import AssetType, SensitivityType, MediumType

class PostStorageInterface(ABC):

    @abstractmethod
    def validate_password_for_user(self, mobile_number: str,
                                   password: str) ->int:
        pass

    @abstractmethod
    def validate_mobile_number(self, mobile_number: str):
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
                            is_flexible: bool,
                            datetime: datetime,
                            from_datetime: datetime,
                            to_datetime: datetime,
                            no_of_seats: int,
                            luggage_quantity: int,
                            user_id: int)->int:
        pass

    @abstractmethod
    def create_asset_transport_request(self,
                                    source: str,
                                    destination: str,
                                    is_flexible: bool,
                                    datetime: datetime,
                                    from_datetime: datetime,
                                    to_datetime: datetime,
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
                            is_flexible: bool,
                            datetime: datetime,
                            from_datetime: datetime,
                            to_datetime: datetime,
                            no_of_seats_available: int,
                            assets_quantity: int,
                            user_id: int):

        pass

    @abstractmethod
    def create_share_travel_info(self,
                                source: str,
                                destination: str,
                                is_flexible: bool,
                                datetime: datetime,
                                from_datetime: datetime,
                                to_datetime: datetime,
                                medium: MediumType,
                                assets_quantity: int,
                                user_id: int):
        pass

    @abstractmethod
    def get_my_ride_requests_dto(self, user_id: int,
                                 limit: int,
                                 offset: int,
                                 asc_order= bool,
                                 sort_by= str,)->List[RideRequestDto]:
        pass


    @abstractmethod
    def get_my_ride_requests_dto_filter_by_active_status_value(self,
                user_id: int,
                limit: int,
                offset: int,
                asc_order= bool,
                sort_by= str)->List[RideRequestDto]:
        pass

    @abstractmethod
    def get_my_ride_requests_dto_filter_by_confirmed_status_value(self,
                user_id: int,
                limit: int,
                offset: int,
                asc_order= bool,
                sort_by= str,)->List[RideRequestDto]:
        pass

    @abstractmethod
    def get_my_ride_requests_dto_filter_by_expired_status_value(self,
                user_id: int,
                limit: int,
                offset: int,
                asc_order: bool,
                sort_by: str)->List[RideRequestDto]:
        pass

    @abstractmethod
    def get_my_asset_requests_dto_filter_by_active_status_value(self,
                user_id: int,
                limit: int,
                offset: int,
                asc_order: bool,
                sort_by: str)->List[RideRequestDto]:
        pass

    @abstractmethod
    def get_my_asset_requests_dto_filter_by_confirmed_status_value(self,
                user_id: int,
                limit: int,
                offset: int,
                asc_order: bool,
                sort_by: str)->List[RideRequestDto]:
        pass

    @abstractmethod
    def get_my_asset_requests_dto_filter_by_expired_status_value(self,
                user_id: int,
                limit: int,
                offset: int,
                asc_order: bool,
                sort_by: str)->List[RideRequestDto]:
        pass


    @abstractmethod
    def get_accepted_persons_dtos(
        self,
        list_of_accepted_persons_ids: List[int])->List[UserDto]:
        pass

    @abstractmethod
    def get_my_asset_requests_dto(
        self, user_id: int,
        limit: int, offset: int,
        asc_order: bool,
        sort_by: str)->List[AssetRequestDto]:
        pass

    @abstractmethod
    def get_total_ride_requests(self, user_id: int)->int:
        pass


    @abstractmethod
    def get_user_ride_shares_from_current_day(self,user_id: int)->[RideShareDto]:
        pass

    @abstractmethod
    def get_total_asset_requests(self, user_id: int)->int:
        pass

    @abstractmethod
    def get_matching_ride_requests_dto_with_flexible_timings(
        self, ride_share_to_datetime: datetime,
        ride_share_from_datetime: datetime,
        ride_share_source: str,
        ride_share_destination: str,
        limit: int, offset: int)->List[RideRequestDto]:
            pass

    @abstractmethod
    def get_matching_ride_requests_dto_without_flexible_timings(
        self, ride_share_datetime: datetime,
        ride_share_source: str,
        ride_share_destination: str,
        limit: int, offset: int)->List[RideRequestDto]:
            pass

    @abstractmethod
    def get_user_dtos(self, matched_persons_ids: List[int])->List[UserDto]:
        pass

    @abstractmethod
    def get_user_travel_info_shares_from_current_day(
        self,
        user_id: int)->List[ShareTravelInfoDto]:
        pass

    @abstractmethod
    def get_matching_asset_requests_dto_with_flexible_timings(
        self, ride_share_to_datetime: datetime,
        ride_share_from_datetime: datetime,
        ride_share_source: str,
        ride_share_destination: str,
        limit: int, offset: int)->List[AssetRequestDto]:
            pass

    @abstractmethod
    def get_matching_asset_requests_dto_without_flexible_timings(
        self, ride_share_datetime: datetime,
        ride_share_source: str,
        ride_share_destination: str,
        limit: int, offset: int)->List[AssetRequestDto]:
            pass
