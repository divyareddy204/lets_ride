from typing import List
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from lets_ride.constants.exception_messages import INVALID_USER_NAME, \
    INVALID_PASSWORD
from lets_ride.interactors.storages.dtos \
    import UserDto, RideRequestWithStatusDto, MyRideRequestsDto,\
    AssetRequestWithStatusDto, MyAssetRequestsDto
from common.dtos import UserAuthTokensDTO
    

class PresenterImplementation(PresenterInterface):

    def create_user_response(self, user_oauth_dto: UserAuthTokensDTO):
        
        user_details = {
            "user_id": user_oauth_dto.user_id,
            "access_token": user_oauth_dto.access_token,
            "refresh_token": user_oauth_dto.refresh_token,
            "expires_in": user_oauth_dto.expires_in
            }
        return user_details
    
    def user_login_response(self, user_access_token_dto: UserAuthTokensDTO):
        
        user_details = {
            "user_id": user_access_token_dto.user_id,
            "access_token": user_access_token_dto.access_token,
            "refresh_token": user_access_token_dto.refresh_token,
            "expires_in": str(user_access_token_dto.expires_in)
            }
        return user_details

    def raise_exception_for_invalid_user(self):

        raise NotFound(*INVALID_USER_NAME)
    
    def raise_exception_for_invalid_password(self):

        raise NotFound(*INVALID_PASSWORD)

    def get_user_profile_response(self, user_profile_dto: UserDto):
        
        user_profile = {
            "user_id": user_profile_dto.user_id,
            "user_name": user_profile_dto.user_name,
            "mobile_number": str(user_profile_dto.mobile_number)
        }
        return user_profile

    def get_my_ride_requests_response(self,
                                      my_ride_request_dto: MyRideRequestsDto,
                                      user_dtos: [UserDto]
                                      ):
        
        my_ride_request_dict = {
            "total_requests": my_ride_request_dto.total_requests,
            "request_dtos": self.get_list_of_ride_requests_dicts(
                my_ride_request_dto.request_dtos,
                ),
            "limit":my_ride_request_dto.limit,
            "offset":my_ride_request_dto.offset
        }
        print("***********************************************************")
        print(my_ride_request_dict)
        return my_ride_request_dict
    
    def convert_user_dto_to_dict(self, user_dto):
        user_dict ={
        "user_name":user_dto.user_name,
        "mobile_number":user_dto.mobile_number
        }
        return user_dict
    
    def get_user_details(self, user_dtos):
        list_user_dicts=[]
        for user_dto in user_dtos:
            user_dict=self.convert_user_dto_to_dict(user_dto)
            list_user_dicts.append(user_dict)
        return list_user_dicts
    
    def convert_ride_request_with_status_dto_to_dict(self,ride_requst_dto_with_status):
        ride_requst_dto_with_status_dict ={
            "ride_request_dto":  self.convert_ride_request_dto_to_dict(
            ride_requst_dto_with_status.ride_request_dto),
            "status" :ride_requst_dto_with_status.status
        }
        return ride_requst_dto_with_status_dict

    def convert_ride_request_dto_to_dict(self, ride_request_dto):
        
        user_dto = self.get_user_dto(self,ride_request_dto.accepted_person_id)
        ride_request_dict= {
            "source": ride_request_dto.source,
            "user_id": ride_request_dto.user_id,
            "destination": ride_request_dto.destination,
            "flexible": ride_request_dto.flexible,
            "datetime": ride_request_dto.datetime,
            "from_datetime": ride_request_dto.from_datetime,
            "to_datetime": ride_request_dto.to_datetime,
            "no_of_seats": ride_request_dto.no_of_seats,
            "luggage_quantity": ride_request_dto.luggage_quantity,
            "accepted_person": self.get_user_details(user_dto)
        }
        return ride_request_dict

    def get_list_of_ride_requests_dicts(self, ride_request_dtos):
        
        list_of_ride_requests=[]
        for ride_request in ride_request_dtos:
            print("********************")
            print (ride_request)
            list_of_ride_requests.append(self.convert_ride_request_with_status_dto_to_dict(
                ride_request
                ))
        return list_of_ride_requests

    def get_my_asset_requests_response(self,
                              my_asset_request_dto: MyAssetRequestsDto):
        
        my_asset_request_dict = {
            "total_requests": my_asset_request_dto.total_requests,
            "request_dtos": self.get_list_of_asset_requests_dicts(
                my_asset_request_dto.request_dtos,
                ),
            "limit":my_asset_request_dto.limit,
            "offset":my_asset_request_dto.offset
        }
        print("***********************************************************")
        print(my_asset_request_dict)
        return my_asset_request_dict
    
    
    def convert_asset_request_with_status_dto_to_dict(self,asset_requst_dto_with_status):
        asset_requst_dto_with_status_dict ={
            "asset_request_dto":  self.convert_asset_request_dto_to_dict(
            asset_requst_dto_with_status.asset_request_dto),
            "status" :asset_requst_dto_with_status.status
        }
        return asset_requst_dto_with_status_dict

    def convert_asset_request_dto_to_dict(self, asset_request_dto):
        user_dto = user_dto_dict[asset_request_dto.accepted_person_id]
        asset_request_dict= {
            "source": asset_request_dto.source,
            "user_id": asset_request_dto.user_id,
            "destination": asset_request_dto.destination,
            "flexible": asset_request_dto.flexible,
            "datetime": asset_request_dto.datetime,
            "from_datetime": asset_request_dto.from_datetime,
            "to_datetime": asset_request_dto.to_datetime,
            "no_of_assets": asset_request_dto.no_of_assets,
            "sensitivity": asset_request_dto.sensitivity,
            "asset_type": asset_request_dto.asset_type,
            "deliver_person": asset_request_dto.deliver_person,
            "accepted_person_id": self.get_user_details(user_dto)
        }
        return asset_request_dict

    def get_list_of_asset_requests_dicts(self, asset_request_dtos):
        
        list_of_asset_requests=[]
        for asset_request in asset_request_dtos:
            print("********************")
            print (asset_request)
            list_of_asset_requests.append(self.convert_asset_request_with_status_dto_to_dict(
                asset_request
                ))
        return list_of_asset_requests

