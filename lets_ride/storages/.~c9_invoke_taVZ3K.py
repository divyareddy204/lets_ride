from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.models import User, RideRequest, \
    AssetTransportRequest, ShareRide, ShareTravelInfo
from lets_ride.exceptions.exceptions import InvalidPassword, \
    InvalidMobileNumber, InvalidUserName
from typing import List
from datetime import datetime
from common.oauth2_storage import OAuth2SQLStorage
from lets_ride.interactors.storages.dtos \
    import UserDto, RideRequestDto, AssetRequestDto
from lets_ride.constants.enums import AssetType, SensitivityType, MediumType


class StorageImplementation(PostStorageInterface):

    def validate_password_for_user(self, mobile_number: str,
                                    password: str):
        try:
            user = User.objects.get(mobile_number=mobile_number)
        except User.DoesNotExist:
            raise InvalidMobileNumber

        if not user.check_password(password):
            raise InvalidPassword
        return user.id

    def validate_mobile_number(self, mobile_number: str):
        try:
            User.objects.get(mobile_number=mobile_number)
        except User.DoesNotExist:
            raise InvalidMobileNumber


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
                            datetime: datetime,
                            from_datetime: datetime,
                            to_datetime: datetime,
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
                                       datetime: datetime,
                                       from_datetime: datetime,
                                       to_datetime: datetime,
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
                        datetime: datetime,
                        from_datetime: datetime,
                        to_datetime: datetime,
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
                        datetime: datetime,
                        from_datetime: datetime,
                        to_datetime: datetime,
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
        print(user_id)
        list_of_ride_request_objs = RideRequest.objects.filter(user_id=user_id)[offset:limit]
        return self.get_ride_request_dtos_for_given_ride_request_objects(
            list_of_ride_request_objs)
    
    def get_my_ride_requests_dto_filter_by_expired_status_value(self,
                user_id: int,
                limit: int,
                offset: int):
        list_of_ride_request_objs = []
        list_of_ride_request_objs.append(RideRequest.objects.filter(
            user_id=user_id,flexible=True,
            to_datetime__lt=datetime.now())[offset:limit])
        
        list_of_ride_request_objs.append(RideRequest.objects.filter(
            user_id=user_id,flexible=False,
            datetime__lt=datetime.now())[offset:limit])
        print("**********566************",list_of_ride_request_objs)
        return self.get_ride_request_dtos_for_given_ride_request_objects(
            list_of_ride_request_objs)

    def get_my_ride_requests_dto_filter_by_active_status_value(self,
            user_id: int,
            limit: int,
            offset: int):
        list_of_ride_request_objs = []
        list_of_ride_request_objs.append(RideRequest.objects.filter(
            user_id=user_id, flexible=True,
            to_datetime__gt=datetime.now())[offset:limit])
        
        list_of_ride_request_objs.append(RideRequest.objects.filter(
            user_id=user_id, flexible=False,
            datetime__gt=datetime.now())[offset:limit])
        return self.get_ride_request_dtos_for_given_ride_request_objects(
            list_of_ride_request_objs)
    
    
    def get_my_ride_requests_dto_filter_by_confirmed_status_value(self,
            user_id: int,
            limit: int,
            offset: int):
        list_of_ride_request_objs = []
        list_of_ride_request_objs.append(RideRequest.objects.filter(
            user_id=user_id,accepted_person__isnull=False)[offset:limit])
        return self.get_ride_request_dtos_for_given_ride_request_objects(
            list_of_ride_request_objs)
        
    def get_my_ride_requests_dto_sort_by_ascending_order(self,
            user_id: int,
            limit: int,
            offset: int,
            sort_by: datetime):
        list_of_ride_request_objs = []
        list_of_ride_request_objs.append(RideRequest.objects.filter(
            user_id=user_id,flexible=True).order_by('to_datetime')[offset:limit].values())
            
        list_of_ride_request_objs.append(RideRequest.objects.filter(
            user_id=user_id,flexible=False).order_by('datetime')[offset:limit].values())

        return self.get_ride_request_dtos_for_given_ride_request_objects(
            list_of_ride_request_objs)
    
    def get_my_ride_requests_dto_sort_by_descending_order(self,
            user_id: int,
            limit: int,
            offset: int,
            sort_by: str):
        list_of_ride_request_objs = []
        list_of_ride_request_objs.append(RideRequest.objects.filter(
            user_id=user_id,flexible=True).order_by('-to_datetime')[offset:limit].values())

        list_of_ride_request_objs.append(RideRequest.objects.filter(
            user_id=user_id,flexible=False).order_by('-datetime')[offset:limit].values())
    
        return self.get_ride_request_dtos_for_given_ride_request_objects(
            list_of_ride_request_objs)

    def get_ride_request_dtos_for_given_ride_request_objects(self,
        list_of_ride_request_objs):
        list_of_ride_requests=[]
        print("***************list_of_ride_request_objs*******************",list_of_ride_request_objs)
        for requests in list_of_ride_request_objs:
           for request in requests:
                if request:
                    if request.flexible:
                        ride_request_dto = RideRequestDto(
                            user_id=request.user_id,
                            source=request.source,
                            destination=request.destination,
                            flexible=request.flexible,
                            datetime=request.datetime,
                            from_datetime=request.from_datetime.replace(tzinfo=None),
                            to_datetime=request.to_datetime.replace(tzinfo=None),
                            no_of_seats=request.no_of_seats,
                            luggage_quantity=request.luggage_quantity,
                            accepted_person_id=request.accepted_person_id
                            )
                        list_of_ride_requests.append(ride_request_dto)
                    else:
                        ride_request_dto = RideRequestDto(
                            user_id=request.user_id,
                            source=request.source,
                            destination=request.destination,
                            flexible=request.flexible,
                            datetime=request.datetime.replace(tzinfo=None),
                            from_datetime=request.from_datetime,
                            to_datetime=request.to_datetime,
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
    
    def get_my_asset_requests_dto_filter_by_expired_status_value(self,
                user_id: int,
                limit: int,
                offset: int):
        list_of_asset_request_objs = []
        list_of_asset_request_objs.append(AssetTransportRequest.objects.filter(
            user_id=user_id,flexible=True,
            to_datetime__lt=datetime.now())[offset:limit])
        
        list_of_asset_request_objs.append(AssetTransportRequest.objects.filter(
            user_id=user_id,flexible=False,
            datetime__lt=datetime.now())[offset:limit])
        print("**********566************",list_of_asset_request_objs)
        return self.get_asset_request_dtos_for_given_asset_request_objects(
            list_of_asset_request_objs)

    def get_my_asset_requests_dto_filter_by_active_status_value(self,
            user_id: int,
            limit: int,
            offset: int):
        list_of_asset_request_objs = []
        list_of_asset_request_objs.append(AssetTransportRequest.objects.filter(
            user_id=user_id, flexible=True,
            to_datetime__gt=datetime.now())[offset:limit])
        
        list_of_asset_request_objs.append(AssetTransportRequest.objects.filter(
            user_id=user_id, flexible=False,
            datetime__gt=datetime.now())[offset:limit])
        return self.get_asset_request_dtos_for_given_asset_request_objects(
            list_of_asset_request_objs)
    
    
    def get_my_asset_requests_dto_filter_by_confirmed_status_value(self,
            user_id: int,
            limit: int,
            offset: int,
            status: str):
        list_of_asset_request_objs = []
        list_of_asset_request_objs.append(AssetTransportRequest.objects.filter(
            user_id=user_id,accepted_person__isnull=False)[offset:limit])
        return self.get_asset_request_dtos_for_given_asset_request_objects(
            list_of_asset_request_objs)
        
    def get_my_asset_requests_dto_sort_by_ascending_order(self,
            user_id: int,
            limit: int,
            offset: int,
            sort_by: datetime):
        list_of_asset_request_objs = []
        list_of_asset_request_objs.append(AssetTransportRequest.objects.filter(
            user_id=user_id,flexible=True).order_by('to_datetime')[offset:limit])
            
        list_of_asset_request_objs.append(AssetTransportRequest.objects.filter(
            user_id=user_id,flexible=False).order_by('datetime')[offset:limit])

        return self.get_asset_request_dtos_for_given_asset_request_objects(
            list_of_asset_request_objs)
    
    def get_my_asset_requests_dto_sort_by_descending_order(self,
            user_id: int,
            limit: int,
            offset: int,
            sort_by: str):
        list_of_asset_request_objs = []
        list_of_asset_request_objs.append(AssetTransportRequest.objects.filter(
            user_id=user_id,flexible=True).order_by('-to_datetime')[offset:limit])

        list_of_asset_request_objs.append(AssetTransportRequest.objects.filter(
            user_id=user_id,flexible=False).order_by('-datetime')[offset:limit])
    
        return self.get_asset_request_dtos_for_given_asset_request_objects(
            list_of_asset_request_objs)
    
    def get_my_asset_requests_dto(self, user_id: int, limit: int, offset: int):
        list_of_asset_request_objs = AssetTransportRequest.objects.filter(
            user_id=user_id)[offset:limit]
        return self.get_asset_request_dtos_for_given_asset_request_objects(
            list_of_asset_request_objs)
    
    def get_asset_request_dtos_for_given_asset_request_objects(self,
        list_of_asset_request_objs):
        list_of_asset_requests=[]
        for request in list_of_asset_request_objs:
            #for request in queryset:
            if request.flexible:
                asset_request_dto = AssetRequestDto(
                    user_id=request.user_id,
                    source=request.source,
                    destination=request.destination,
                    flexible=request.flexible,
                    datetime=request.datetime,
                    from_datetime=request.from_datetime.replace(tzinfo=None),
                    to_datetime=request.to_datetime.replace(tzinfo=None),
                    no_of_assets=request.no_of_assets,
                    asset_type=request.asset_type,
                    sensitivity=request.sensitivity,
                    deliver_person=request.deliver_person,
                    accepted_person_id=request.accepted_person_id
                    )
                list_of_asset_requests.append(asset_request_dto)
            else:
                asset_request_dto = AssetRequestDto(
                    user_id=request.user_id,
                    source=request.source,
                    destination=request.destination,
                    flexible=request.flexible,
                    datetime=request.datetime.replace(tzinfo=None),
                    from_datetime=request.from_datetime,
                    to_datetime=request.to_datetime,
                    no_of_assets=request.no_of_assets,
                    asset_type=request.asset_type,
                    sensitivity=request.sensitivity,
                    deliver_person=request.deliver_person,
                    accepted_person_id=request.accepted_person_id
                    )
                list_of_asset_requests.append(asset_request_dto)
        return list_of_asset_requests

    
    def get_accepted_persons_dtos(self, list_of_accepted_persons_ids: List[int]):
        user_dtos_list = []
        if list_of_accepted_persons_ids:
            user_objs = list(User.objects.filter(id__in=list_of_accepted_persons_ids))
            for user_obj in user_objs:
                user_dto = UserDto(
                    user_id=user_obj.id,
                    user_name=user_obj.user_name,
                    mobile_number=user_obj.mobile_number
                    )
                user_dtos_list.append(user_dto)
        return user_dtos_list
    
    """def get_matching_ride_requests_dto(self, user_id:int):
        from django.db.models import Q
        share_objects=ShareRide.objects.filter(user_id=user_id,datetime>datetime.now())
        for share_obj in share_objects:
            list_of_ride_request_objs=RideRequest.objects.filter(
                Q(share_object.source=source),
                Q(share_object.destinatiom=destination) | Q(share_object.datetime=dateme),
                Q(share_object.from_datetime=from_datetime),
                Q(share_object.to_datetime=to_datetime)
                )

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
        return list_of_ride_requests"""

    def get_matching_ride_requests_dto(self, user_id:int):
        pass
        
    
    def get_user_dtos(self, matched_persons_ids: List[int]):
        user_dtos_list = []
        if matched_persons_ids:
            user_objs = list(User.objects.filter(id__in=[matched_persons_ids]))
            for user_obj in user_objs:
                user_dto = UserDto(
                    user_id=user_obj.id,
                    user_name=user_obj.user_name,
                    mobile_number=user_obj.mobile_number
                    )
                user_dtos_list.append(user_dto)
        return user_dtos_list
        