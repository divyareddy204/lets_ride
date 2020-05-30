from abc import ABC
from abc import abstractmethod
from common.dtos import UserAuthTokensDTO
from lets_ride.interactors.storages.dtos \
    import UserDto, RideRequestWithStatusDto, RideRequestDto, \
    MyRideRequestsDto, MyAssetRequestsDto


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
    def raise_exception_for_invalid_user(self):
        pass

    @abstractmethod
    def get_user_profile_response(self, user_dto: UserDto):
        pass
    
    @abstractmethod
    def get_my_ride_requests_response(self,
                                      my_ride_request_dto: MyRideRequestsDto):
        pass
    
    @abstractmethod
    def get_my_asset_requests_response(self,
                                      user_dtos: [UserDto],
                                      my_asset_request_dto: MyAssetRequestsDto):
        pass