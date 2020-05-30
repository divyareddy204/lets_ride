from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.models import User, RideRequest, \
    AssetTransportRequest, ShareRide, ShareTravelInfo
from lets_ride.exceptions.exceptions import InvalidPassword, \
    InvalidUserName
from typing import List
from common.oauth2_storage import OAuth2SQLStorage
from lets_ride.interactors.storages.dtos \
    import UserDto, RideRequestDto, AssetRequestDto
from lets_ride.constants.enums import AssetType, SensitivityType, MediumType

class StorageImplementation(PostStorageInterface):

    def validate_password_for_user(self, user_name: str,
                                    password: str):
        try:
            user = User.objects.get(user_name=user_name)
        except User.DoesNotExist:
            raise InvalidUserName

        if not user.check_password(password):
            raise InvalidPassword
        return user.id

    def validate_user_name(self, user_name: str):
        try:
            User.objects.get(user_name=user_name)
        except User.DoesNotExist:
            raise InvalidUserName


    def create_user(self, user_name: str, mobile_number: str, password: str):
        
        User.objects.create(user_name=user_name,
                            mobile_number=mobile_number,
                            password=password)

    def get_user_profile(self, user_name: str):
        
        try:
            user = User.Objects.get(user_name=user_name)
        except User.DoesNotExist:
            raise InvalidUserName
        
        user_dto = self._get_user_dto(user)
        return user_dto

    def create_ride_request(self,
                            source: str,
                            destination: str,
                            flexible: bool,
                            datetime: str,
                            from_datetime: str,
                            to_datetime: str,
                            no_of_seats: int,
                            luggage_quantity: int,
                            user_id: int):

        RideRequest.objects.create(
            source=source,
            destination=destination ,
            flexible=flexible,
            datetime=datetime,
            from_datetime=from_datetime,
            to_datetime=to_datetime,
            user_id=user_id,
            no_of_seats=no_of_seats,
            luggage_quantity=luggage_quantity
           )
        print("ride_request_created")

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
        AssetTransportRequest.objects.create(
            source=source,
            destination=destination ,
            flexible=flexible,
            datetime=datetime,
            from_datetime=from_datetime,
            to_datetime=to_datetime,
            user_id=user_id,
            no_of_assets=no_of_assets,
            asset_type=asset_type,
            sensitivity=sensitivity,
            deliver_person=deliver_person
            )

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
            ShareRide.objects.create(
                source=source,
                destination=destination ,
                flexible=flexible,
                datetime=datetime,
                from_datetime=from_datetime,
                to_datetime=to_datetime,
                user_id=user_id,
                no_of_seats_available=no_of_seats_available,
                assets_quantity= assets_quantity
               )

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

            ShareTravelInfo.objects.create(
                source=source,
                destination=destination ,
                flexible=flexible,
                datetime=datetime,
                from_datetime=from_datetime,
                to_datetime=to_datetime,
                user_id=user_id,
                medium = medium,
                assets_quantity= assets_quantity
               )

    def _get_user_dto(self, user_obj):
        user_dto = UserDto(
            user_id=user_obj.id,
            user_name=user_obj.user_name,
            mobile_number=user_obj.mobile_number)
        return user_dto

    def get_my_ride_requests_dto(self, user_id: int, limit: int, offset: int):
        list_of_ride_request_objs = RideRequest.objects.filter(user_id=user_id)[offset:limit]
        list_of_ride_requests=[]
        for request in list_of_ride_request_objs:
            ride_request_dto = RideRequestDto(
                user_id=request.user_id,
                source=request.source,
                destination=request.destination,
                flexible=request.flexible,
                datetime=str(request.datetime),
                from_datetime=str(request.from_datetime),
                to_datetime=str(request.to_datetime),
                no_of_seats=request.no_of_seats,
                luggage_quantity=request.luggage_quantity,
                accepted_person_id=request.accepted_person_id
                )
            list_of_ride_requests.append(ride_request_dto)
        return list_of_ride_requests

    def get_total_requests(self):
        return RideRequest.objects.all().count()
    
    def get_total_asset_requests(self):
        return AssetTransportRequest.objects.all().count()

    def get_my_asset_requests_dto(self, user_id: int):
        list_of_asset_request_objs = AssetTransportRequest.objects.filter(
            user_id=user_id)
        list_of_asset_requests=[]
        for request in list_of_asset_request_objs:
            asset_request_dto = AssetRequestDto(
                user_id=request.user_id,
                source=request.source,
                destination=request.destination,
                flexible=request.flexible,
                datetime=str(request.datetime),
                from_datetime=str(request.from_datetime),
                to_datetime=str(request.to_datetime),
                no_of_assets=request.no_of_assets,
                asset_type= request.asset_type,
                sensitivity= request.sensitivity,
                deliver_person= request.deliver_person,
                accepted_person_id=request.accepted_person_id
                )
            list_of_asset_requests.append(asset_request_dto)
        return list_of_asset_requests

    
    def get_accepted_persons_dtos(self, list_of_accepted_persons_ids: List[int]):
        
        user_objs = list(User.objects.filter(id__in=[list_of_accepted_persons_ids]))
        user_dtos_list = []
        for user_obj in user_objs:
            user_dto = UserDto(
                user_id=user_obj.id,
                user_name=user_obj.user_name,
                mobile_number=user_obj.mobile_number
                )
            user_dtos_list.append(user_dto)
        return user_dtos_list