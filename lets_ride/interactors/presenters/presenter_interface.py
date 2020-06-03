from abc import ABC
from abc import abstractmethod
from common.dtos import UserAuthTokensDTO
from lets_ride.interactors.storages.dtos \
    import UserDto, RideRequestWithStatusDto, RideRequestDto, \
    MyRideRequestsDto, MyAssetRequestsDto, AssetRequestDto


class PresenterInterface(ABC):

    @abstractmethod
    def create_user_response(self, user_access_dto: UserAuthTokensDTO):
        pass
    
    @abstractmethod
    def user_login_response(self, user_access_token_dto: UserAuthTokensDTO):
        pass
    
    @abstractmethod
    def raise_exception_for_invalid_password(self):
        pass
    
    @abstractmethod
    def raise_exception_for_invalid_mobile_number(self):
        pass

    @abstractmethod
    def get_user_profile_response(self, user_dto: UserDto):
        pass
    
    @abstractmethod
    def get_my_ride_requests_response(self,
                                      my_ride_request_dto: MyRideRequestsDto,
                                      user_dtos: [UserDto]):
        pass
    
    @abstractmethod
    def get_my_asset_requests_response(self,
                                      user_dtos: [UserDto],
                                      my_asset_request_dto: MyAssetRequestsDto):
        pass
    @abstractmethod
    def get_response_for_matching_ride_requests(
        self,matching_ride_requests: [RideRequestDto],
        matched_user_dtos: UserDto):
        pass
    
    @abstractmethod
    def get_response_for_matching_asset_requests(
        self,matching_asset_requests: [AssetRequestDto],
        matched_user_dtos: UserDto):
        pass