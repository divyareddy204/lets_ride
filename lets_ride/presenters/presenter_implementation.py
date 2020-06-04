from typing import List
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from django_swagger_utils.drf_server.exceptions import BadRequest
from lets_ride.constants.exception_messages import INVALID_LIMIT,\
    INVALID_OFFSET, INVALID_MOBILE_NUMBER,INVALID_PASSWORD
from lets_ride.interactors.storages.dtos \
    import UserDto, RideRequestWithStatusDto, MyRideRequestsDto,\
    AssetRequestWithStatusDto, MyAssetRequestsDto, \
    RideRequestDto, AssetRequestDto
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

    def raise_exception_for_invalid_limit(self):
        raise BadRequest(*INVALID_LIMIT)

    def raise_exception_for_invalid_offset(self):
        raise BadRequest(*INVALID_OFFSET)

    def user_login_response(self, user_access_token_dto: UserAuthTokensDTO):

        user_details = {
            "user_id": user_access_token_dto.user_id,
            "access_token": user_access_token_dto.access_token,
            "refresh_token": user_access_token_dto.refresh_token,
            "expires_in": str(user_access_token_dto.expires_in)
            }
        return user_details

    def raise_exception_for_invalid_mobile_number(self):

        raise BadRequest(*INVALID_MOBILE_NUMBER)

    def raise_exception_for_invalid_password(self):

        raise BadRequest(*INVALID_PASSWORD)

    def get_user_profile_response(self, user_profile_dto: UserDto):

        user_profile = {
            "user_id": user_profile_dto.user_id,
            "user_name": user_profile_dto.user_name,
            "mobile_number": str(user_profile_dto.mobile_number)
        }
        return user_profile

    def get_my_ride_requests_response(self,
                                      my_ride_request_dto: MyRideRequestsDto,
                                      user_dtos: List[UserDto]
                                      ):
        my_ride_request_dict = {
            "total_requests": my_ride_request_dto.total_requests,
            "requests": self.get_list_of_ride_requests_dicts(
                my_ride_request_dto.request_dtos,user_dtos
                ),
            "limit":my_ride_request_dto.limit,
            "offset":my_ride_request_dto.offset
        }
        return my_ride_request_dict

    def get_list_of_ride_requests_dicts(self,
        ride_request_dtos_with_status,
        user_dtos):
        list_of_status_dicts =[]
        for ride_request_with_status in ride_request_dtos_with_status:
            list_of_status_dicts.append(self.convert_ride_request_dto_to_dict(
                ride_request_with_status.ride_request_dto,
                ride_request_with_status.status, user_dtos))
        return list_of_status_dicts


    def convert_ride_request_dto_to_dict(self, ride_request_dto,
        status, user_dtos):
        user_dict ={}
        for user_dto in user_dtos:
            if(ride_request_dto.accepted_person_id==user_dto.user_id):
                user_dict=self.get_accepted_persons_details_dict(user_dto)
        ride_request_dict= {
            "source": ride_request_dto.source,
            "user_id": ride_request_dto.user_id,
            "destination": ride_request_dto.destination,
            "is_flexible": ride_request_dto.is_flexible,
            "datetime": str(ride_request_dto.datetime),
            "from_datetime": str(ride_request_dto.from_datetime),
            "to_datetime": str(ride_request_dto.to_datetime),
            "no_of_seats": ride_request_dto.no_of_seats,
            "luggage_quantity": ride_request_dto.luggage_quantity,
            "accepted_person": user_dict,
            "status": status
        }
        return ride_request_dict

    def get_accepted_persons_details_dict(self,user_dto):
       return  self.convert_user_dto_to_dict(user_dto)

    def get_my_asset_requests_response(self,
                                      my_asset_request_dto: MyAssetRequestsDto,
                                      user_dtos: List[UserDto]
                                      ):
        my_asset_request_dict = {
            "total_requests": my_asset_request_dto.total_requests,
            "requests": self.get_list_of_asset_requests_dicts(
                my_asset_request_dto.request_dtos,user_dtos
                ),
            "limit":my_asset_request_dto.limit,
            "offset":my_asset_request_dto.offset
        }
        return my_asset_request_dict

    def get_list_of_asset_requests_dicts(self,
        asset_request_dtos_with_status,
        user_dtos):
        list_of_status_dicts =[]
        for asset_request_with_status in asset_request_dtos_with_status:
            list_of_status_dicts.append(self.convert_asset_request_dto_to_dict(
                asset_request_with_status.asset_request_dto,
                asset_request_with_status.status, user_dtos))
        return list_of_status_dicts


    def convert_asset_request_dto_to_dict(self, asset_request_dto,
        status, user_dtos):
        user_dict ={}
        for user_dto in user_dtos:
            if(asset_request_dto.accepted_person_id==user_dto.user_id):
                user_dict=self.get_accepted_persons_details_dict(user_dto)

        asset_request_dict= {
            "source": asset_request_dto.source,
            "user_id": asset_request_dto.user_id,
            "destination": asset_request_dto.destination,
            "is_flexible": asset_request_dto.is_flexible,
            "datetime": str(asset_request_dto.datetime),
            "from_datetime": str(asset_request_dto.from_datetime),
            "to_datetime": str(asset_request_dto.to_datetime),
            "no_of_assets": asset_request_dto.no_of_assets,
            "sensitivity": asset_request_dto.sensitivity,
            "asset_type": asset_request_dto.asset_type,
            "deliver_person": asset_request_dto.deliver_person,
            "accepted_person": user_dict,
            "status": status
        }
        return asset_request_dict

    def convert_user_dto_to_dict(self, user_dto):
        if user_dto:
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

    def get_response_for_matching_ride_requests(
        self,matching_ride_requests: [RideRequestDto],
        matched_user_dtos: UserDto, limit: int, offset:int):
        list_of_ride_request_dicts =[self.
        convert_matching_ride_request_dto_to_dict(ride_request_dto,
        matched_user_dtos) for ride_request_dto in matching_ride_requests]
        matching_rides = {
            "matching_ride_requests": list_of_ride_request_dicts,
            "limit": limit,
            "offset": offset,
        }
        return matching_rides

    def convert_matching_ride_request_dto_to_dict(self,ride_request_dto,user_dtos):
        user_dict ={}
        for user_dto in user_dtos:
            if(ride_request_dto.user_id==user_dto.user_id):
                user_dict=self.convert_user_dto_to_dict(user_dto)

        ride_request_dict= {
            "source": ride_request_dto.source,
            "user_id": ride_request_dto.user_id,
            "destination": ride_request_dto.destination,
            "is_flexible": ride_request_dto.is_flexible,
            "datetime": str(ride_request_dto.datetime),
            "from_datetime": str(ride_request_dto.from_datetime),
            "to_datetime": str(ride_request_dto.to_datetime),
            "no_of_seats": ride_request_dto.no_of_seats,
            "luggage_quantity": ride_request_dto.luggage_quantity,
            "accepted_person": user_dict,
        }
        return ride_request_dict

    def get_response_for_matching_asset_requests(
        self,matching_asset_requests: [AssetRequestDto],
        matched_user_dtos: UserDto, limit: int, offset: int):

        list_of_asset_request_dicts =[self.\
        convert_matching_asset_request_dto_to_dict(
            asset_request_dto,matched_user_dtos) for asset_request_dto
            in matching_asset_requests]
        matching_assets = {
            "matching_asset_requests": list_of_asset_request_dicts,
            "limit": limit,
            "offset": offset,
        }
        return matching_assets

    def convert_matching_asset_request_dto_to_dict(self,asset_request_dto,user_dtos):
        user_dict ={}
        for user_dto in user_dtos:
            if(asset_request_dto.user_id==user_dto.user_id):
                user_dict=self.convert_user_dto_to_dict(user_dto)

        asset_request_dict= {
            "source": asset_request_dto.source,
            "user_id": user_dict,
            "destination": asset_request_dto.destination,
            "is_flexible": asset_request_dto.is_flexible,
            "datetime": str(asset_request_dto.datetime),
            "from_datetime": str(asset_request_dto.from_datetime),
            "to_datetime": str(asset_request_dto.to_datetime),
            "no_of_assets": asset_request_dto.no_of_assets,
            "asset_type": asset_request_dto.asset_type,
            "sensitivity":asset_request_dto.sensitivity,
            "deliver_person": asset_request_dto.deliver_person,
        }
        return asset_request_dict
