from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.models import User, RideRequest, \
    AssetTransportRequest, ShareRide, ShareTravelInfo
from lets_ride.exceptions.exceptions import InvalidPassword, \
    InvalidUserName
from common.oauth2_storage import OAuth2SQLStorage
from lets_ride.interactors.storages.dtos import UserDto, RideRequestDto
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

    def get_my_ride_requests_dto(self, user_id: int)->int:
        list_of_ride_requests = RideRequest.objects.get(user_id=user_id)
        list_of_
        for request in list_of_ride_requests:
            ride_request_dto = RideRequestDto(
                user_id=request.user_id,
                source=request.source,
                destination=request.destination,
                flexible=request.flexible,
                datetime=request.datetime,
                from_datetime=request.from_datetime,
                to_datetime=request.to_datetime,
                no_of_seats=request.no_of_seats,
                assets_quantity=request.assets_quantity,
                

        return 
    def 