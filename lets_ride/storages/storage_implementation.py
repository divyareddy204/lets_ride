from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.models import User, RideRequest, \
    AssetTransportRequest, ShareRide, ShareTravelInfo
from lets_ride.exceptions.exceptions import InvalidPassword, \
    InvalidMobileNumber, InvalidUserName
from typing import List
import datetime
from django.db.models import Q, Case, CharField, Value, When
from common.oauth2_storage import OAuth2SQLStorage
from lets_ride.interactors.storages.dtos \
    import UserDto, RideRequestDto, AssetRequestDto, RideRequestDto,\
    RideShareDto, ShareTravelInfoDto
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
                            is_flexible: bool,
                            datetime: datetime,
                            from_datetime: datetime,
                            to_datetime: datetime,
                            no_of_seats: int,
                            luggage_quantity: int,
                            user_id: int):

        RideRequest.objects.create(
            source=source,
            destination=destination ,
            is_flexible=is_flexible,
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
                                       is_flexible: bool,
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
            is_flexible=is_flexible,
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
                        is_flexible: bool,
                        datetime: datetime,
                        from_datetime: datetime,
                        to_datetime: datetime,
                        no_of_seats_available: int,
                        assets_quantity: int,
                        user_id: int):

            ShareRide.objects.create(
                source=source,
                destination=destination ,
                is_flexible=is_flexible,
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
                        is_flexible: bool,
                        datetime: datetime,
                        from_datetime: datetime,
                        to_datetime: datetime,
                        medium: MediumType,
                        assets_quantity: int,
                        user_id: int):

            ShareTravelInfo.objects.create(
                source=source,
                destination=destination ,
                is_flexible=is_flexible,
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

    def get_my_ride_requests_dto(
        self, user_id: int,
        limit: int, offset: int,
        asc_order: bool, sort_by: str):
        if sort_by=="datetime":
            list_of_ride_request_objs = RideRequest.objects.filter(
                user_id=user_id).annotate(
                    sorting_datetime=Case(
                        When(is_flexible=True, then=Value("from_datetime")),
                        When(is_flexible=False, then=Value("datetime")),
                        default=Value('datetime'),
                        output_field=CharField(),
                    )).order_by(
                        ("" if asc_order else "-") +"sorting_datetime")\
                        [offset:limit]
        else:
            list_of_ride_request_objs = RideRequest.objects.filter(
                user_id=user_id).order_by(
                    (""if asc_order else "-") + "no_of_seats")[offset:limit]

        return self.get_ride_request_dtos_for_given_ride_request_objects(
            list_of_ride_request_objs)

    def get_my_ride_requests_dto_filter_by_expired_status_value(self,
                user_id: int,
                limit: int,
                offset: int,
                asc_order: bool,
                sort_by: str):

        if sort_by =="datetime":
            list_of_ride_request_objs = RideRequest.objects.filter(
                Q(to_datetime__lt=datetime.datetime.now(),
                  is_flexible=True,)|Q(datetime__lt=datetime.datetime.now(),
                is_flexible=False),user_id=user_id).annotate(
                    sorting_datetime=Case(
                        When(is_flexible=True, then=Value("from_datetime")),
                        When(is_flexible=False, then=Value("datetime")),
                        default=Value('datetime'),
                        output_field=CharField(),
                    )).order_by(
                        ("" if asc_order else "-") +"sorting_datetime")\
                        [offset:limit]
        else:
            list_of_ride_request_objs = RideRequest.objects.filter(
                Q(to_datetime__lt=datetime.datetime.now(),is_flexible=True,)|Q(
                datetime__lt=datetime.datetime.now(),
                is_flexible=False),user_id=user_id)\
                .order_by(
                    (""if asc_order else "-") + "no_of_seats")[offset:limit]
            

        return self.get_ride_request_dtos_for_given_ride_request_objects(
            list_of_ride_request_objs)

    def get_my_ride_requests_dto_filter_by_active_status_value(self,
            user_id: int,
            limit: int,
            offset: int,
            asc_order: bool,
            sort_by: str):
        if sort_by =="datetime":
            list_of_ride_request_objs = RideRequest.objects.filter(
                Q(to_datetime__gt=datetime.datetime.now(),is_flexible=True,)\
                |Q(datetime__gt=datetime.datetime.now(),
                is_flexible=False),user_id=user_id).annotate(
                    sorting_datetime=Case(
                        When(is_flexible=True, then=Value("from_datetime")),
                        When(is_flexible=False, then=Value("datetime")),
                        default=Value('datetime'),
                        output_field=CharField(),
                    )).order_by(
                        ("" if asc_order else "-") +"sorting_datetime")\
                        [offset:limit]
        else:
            list_of_ride_request_objs = RideRequest.objects.filter(
                Q(to_datetime__gt=datetime.datetime.now(),is_flexible=True,)|Q(
                datetime__gt=datetime.datetime.now(),
                is_flexible=False),user_id=user_id)\
                .order_by((""if asc_order else "-") + "no_of_seats")[offset:limit]
                
        return self.get_ride_request_dtos_for_given_ride_request_objects(
            list_of_ride_request_objs)

    def get_my_ride_requests_dto_filter_by_confirmed_status_value(self,
            user_id: int,
            limit: int,
            offset: int,
            sort_by: str,
            asc_order: bool):

        if sort_by =="datetime":
            list_of_ride_request_objs = RideRequest.objects.filter(
                user_id=user_id,accepted_person__isnull=False).annotate(
                    sorting_datetime=Case(
                            When(is_flexible=True, then=Value("from_datetime")),
                            When(is_flexible=False, then=Value("datetime")),
                            default=Value('datetime'),
                            output_field=CharField(),
                        )).order_by(
                            ("" if asc_order else "-") +"sorting_datetime")\
                            [offset:limit]
        else:
            list_of_ride_request_objs = RideRequest.objects.filter(
                user_id=user_id,accepted_person__isnull=False)\
                .order_by(("" if asc_order else "-") +"sorting_datetime")\
                [offset:limit]
            
        return self.get_ride_request_dtos_for_given_ride_request_objects(
            list_of_ride_request_objs)

    def get_ride_request_dtos_for_given_ride_request_objects(self,
            list_of_ride_request_objs):
        list_of_ride_requests=[]
        for request in list_of_ride_request_objs:
            if request:
                if request.is_flexible:
                    ride_request_dto = self.\
                    convert_ride_request_obj_to_dto_with_flexible_timings(request)
                    list_of_ride_requests.append(ride_request_dto)
                else:
                    ride_request_dto = self.\
                    convert_ride_request_obj_to_dto_without_flexible_timings(request)
                    list_of_ride_requests.append(ride_request_dto)
        return list_of_ride_requests

    def convert_ride_request_obj_to_dto_with_flexible_timings(self, request):
        ride_request_dto=RideRequestDto(
            user_id=request.user_id,
            source=request.source,
            destination=request.destination,
            is_flexible=request.is_flexible,
            datetime=request.datetime,
            from_datetime=request.from_datetime.replace(tzinfo=None),
            to_datetime=request.to_datetime.replace(tzinfo=None),
            no_of_seats=request.no_of_seats,
            luggage_quantity=request.luggage_quantity,
            accepted_person_id=request.accepted_person_id
            )
        return ride_request_dto

    def convert_ride_request_obj_to_dto_without_flexible_timings(self, request):
        ride_request_dto = RideRequestDto(
            user_id=request.user_id,
            source=request.source,
            destination=request.destination,
            is_flexible=request.is_flexible,
            datetime=request.datetime.replace(tzinfo=None),
            from_datetime=request.from_datetime,
            to_datetime=request.to_datetime,
            no_of_seats=request.no_of_seats,
            luggage_quantity=request.luggage_quantity,
            accepted_person_id=request.accepted_person_id
            )
        return ride_request_dto

    def get_total_ride_requests(self, user_id: int ):
        return RideRequest.objects.filter(user_id=user_id).count()

    def get_total_asset_requests(self, user_id: int):
        return AssetTransportRequest.objects.filter(user_id=user_id).count()

    def get_my_asset_requests_dto_filter_by_expired_status_value(self,
                user_id: int,
                limit: int,
                offset: int):
        list_of_asset_request_objs = AssetTransportRequest.objects.filter(
            Q(is_flexible=True,to_datetime__lt=datetime.datetime.now())|
            Q(is_flexible=False, datetime__lt=datetime.datetime.now()),
            user_id=user_id)[offset:limit]
        return self.get_asset_request_dtos_for_given_asset_request_objects(
            list_of_asset_request_objs)

    def get_my_asset_requests_dto_filter_by_active_status_value(self,
            user_id: int,
            limit: int,
            offset: int,
            sort_by: str,
            asc_order: bool
            ):
    
        if sort_by:
            list_of_asset_request_objs = AssetTransportRequest.objects.filter(
                Q(is_flexible=True,to_datetime__gt=datetime.datetime.now())|
                Q(is_flexible=False, datetime__gt=datetime.datetime.now()),
                user_id=user_id).annotate(
                        sorting_datetime=Case(
                            When(is_flexible=True, then=Value("from_datetime")),
                            When(is_flexible=False, then=Value("datetime")),
                            default=Value('datetime'),
                            output_field=CharField(),
                        )).order_by(
                            ("" if asc_order else "-") +"sorting_datetime")\
                            [offset:limit]
        else:
            list_of_asset_request_objs = AssetTransportRequest.objects.filter(
                Q(is_flexible=True,to_datetime__gt=datetime.datetime.now())|
                Q(is_flexible=False, datetime__gt=datetime.datetime.now()),
                user_id=user_id).order_by(
                            ("" if asc_order else "-") +"no_of_assets")\
                            [offset:limit]

        return self.get_asset_request_dtos_for_given_asset_request_objects(
            list_of_asset_request_objs)

    def get_my_asset_requests_dto_filter_by_confirmed_status_value(self,
            user_id: int,
            limit: int,
            offset: int,
            sort_by: str,
            asc_order: bool):
        if sort_by == "datetime":
            list_of_asset_request_objs = AssetTransportRequest.objects.filter(
                user_id=user_id,accepted_person__isnull=False).annotate(
                        sorting_datetime=Case(
                            When(is_flexible=True, then=Value("from_datetime")),
                            When(is_flexible=False, then=Value("datetime")),
                            default=Value('datetime'),
                            output_field=CharField(),
                        )).order_by(
                            ("" if asc_order else "-") +"sorting_datetime")\
                            [offset:limit]
        else:
            list_of_asset_request_objs = AssetTransportRequest.objects.filter(
                user_id=user_id,accepted_person__isnull=False).order_by(
                            ("" if asc_order else "-") +"no_of_assets")\
                            [offset:limit]

        return self.get_asset_request_dtos_for_given_asset_request_objects(
            list_of_asset_request_objs)

    
    def get_my_asset_requests_dto(
        self, user_id: int,
        limit: int, offset: int,
        asc_order: bool, sort_by: str):
        if sort_by == "datetime":
            list_of_asset_request_objs = AssetTransportRequest.objects.filter(
                user_id=user_id).annotate(
                            sorting_datetime=Case(
                                When(is_flexible=True, then=Value("from_datetime")),
                                When(is_flexible=False, then=Value("datetime")),
                                default=Value('datetime'),
                                output_field=CharField(),
                            )).order_by(
                                ("" if asc_order else "-") +"sorting_datetime")\
                                [offset:limit]
        else:
            list_of_asset_request_objs = AssetTransportRequest.objects.filter(
                user_id=user_id).order_by(
                    ("" if asc_order else "-") +"sorting_datetime")\
                    [offset:limit]
            
        return self.get_asset_request_dtos_for_given_asset_request_objects(
            list_of_asset_request_objs)

    def get_asset_request_dtos_for_given_asset_request_objects(self,
        list_of_asset_request_objs):
        list_of_asset_requests=[]
        for request in list_of_asset_request_objs:
            if request.is_flexible:
                asset_request_dto = self.\
                convert_asset_request_obj_to_dto_with_flexible_timings(request)
                list_of_asset_requests.append(asset_request_dto)
            else:
                asset_request_dto = self.\
                convert_asset_request_obj_to_dto_without_flexible_timings(request)
                list_of_asset_requests.append(asset_request_dto)
        return list_of_asset_requests

    def convert_asset_request_obj_to_dto_with_flexible_timings(self,request):
        asset_request_dto =AssetRequestDto(
            user_id=request.user_id,
            source=request.source,
            destination=request.destination,
            is_flexible=request.is_flexible,
            datetime=request.datetime,
            from_datetime=request.from_datetime.replace(tzinfo=None),
            to_datetime=request.to_datetime.replace(tzinfo=None),
            no_of_assets=request.no_of_assets,
            asset_type=request.asset_type,
            sensitivity=request.sensitivity,
            deliver_person=request.deliver_person,
            accepted_person_id=request.accepted_person_id
            )
        return asset_request_dto

    def convert_asset_request_obj_to_dto_without_flexible_timings(self, request):
        asset_request_dto =AssetRequestDto(
            user_id=request.user_id,
            source=request.source,
            destination=request.destination,
            is_flexible=request.is_flexible,
            datetime=request.datetime.replace(tzinfo=None),
            from_datetime=request.from_datetime,
            to_datetime=request.to_datetime,
            no_of_assets=request.no_of_assets,
            asset_type=request.asset_type,
            sensitivity=request.sensitivity,
            deliver_person=request.deliver_person,
            accepted_person_id=request.accepted_person_id
            )
        return asset_request_dto

    def get_accepted_persons_dtos(self,
    list_of_accepted_persons_ids: List[int]):
        user_dtos_list = []
        if list_of_accepted_persons_ids:
            user_objs = list(User.objects.filter(
                id__in=list_of_accepted_persons_ids))
            for user_obj in user_objs:
                user_dto = UserDto(
                    user_id=user_obj.id,
                    user_name=user_obj.user_name,
                    mobile_number=user_obj.mobile_number
                    )
                user_dtos_list.append(user_dto)
        return user_dtos_list


    def get_user_ride_shares_from_current_day(self, user_id: int):
        current_datetime= datetime.datetime.now()
        ride_share_objects=ShareRide.objects\
        .filter(Q(is_flexible=False,datetime__gt=current_datetime)|\
        Q(is_flexible=True,to_datetime__gt=current_datetime),user_id=user_id)
        return self.convert_ride_share_objects_to_list_of_dtos(ride_share_objects)

    def convert_ride_share_objects_to_list_of_dtos(self, share_objs):
        list_of_share_dtos=[]
        for share_obj in share_objs:
            share_dto = self.convert_share_object_to_dto(share_obj)
            list_of_share_dtos.append(share_dto)
        return list_of_share_dtos

    def convert_share_object_to_dto(self,share_object):
        ride_share_dto = RideShareDto(
            user_id=share_object.user_id,
            source=share_object.source,
            destination=share_object.destination,
            is_flexible=share_object.is_flexible,
            datetime=share_object.datetime,
            from_datetime=share_object.from_datetime,
            to_datetime=share_object.to_datetime,
            no_of_seats_available=share_object.no_of_seats_available,
            assets_quantity=share_object.assets_quantity,
            )
        return ride_share_dto

    def get_matching_ride_requests_dto_with_flexible_timings(
        self,
        ride_share_to_datetime: datetime,
        ride_share_from_datetime: datetime,
        ride_share_source: str,ride_share_destination: str,
        limit: int, offset: int
        ):

        matching_ride_request_objs = RideRequest.objects.filter(
            Q(from_datetime__gte=ride_share_from_datetime,
              from_datetime__lte=ride_share_to_datetime)|
            Q(to_datetime__lte=ride_share_to_datetime,
              to_datetime__gtee=ride_share_from_datetime),
            source=ride_share_source,destination=ride_share_destination
            )[offset:limit]

        list_of_ride_requests=[]
        for request in matching_ride_request_objs:
            ride_request_dto = RideRequestDto(
                user_id=request.user_id,
                source=request.source,
                destination=request.destination,
                is_flexible=request.is_flexible,
                datetime=str(request.datetime),
                from_datetime=str(request.from_datetime),
                to_datetime=str(request.to_datetime),
                no_of_seats=request.no_of_seats,
                luggage_quantity=request.luggage_quantity,
                accepted_person_id=request.accepted_person_id
                )
            list_of_ride_requests.append(ride_request_dto)
        return list_of_ride_requests

    def get_matching_ride_requests_dto_without_flexible_timings(
        self,
        ride_share_datetime: datetime,
        ride_share_source: str, ride_share_destination: str,
        limit: int, offset: int):

        matching_ride_request_objs = RideRequest.objects.filter(
            datetime=ride_share_datetime,
            source=ride_share_source,
            destination=ride_share_destination
            )[offset:limit]

        list_of_ride_requests=[]
        for request in matching_ride_request_objs:
            ride_request_dto = RideRequestDto(
                user_id=request.user_id,
                source=request.source,
                destination=request.destination,
                is_flexible=request.is_flexible,
                datetime=str(request.datetime),
                from_datetime=str(request.from_datetime),
                to_datetime=str(request.to_datetime),
                no_of_seats=request.no_of_seats,
                luggage_quantity=request.luggage_quantity,
                accepted_person_id=request.accepted_person_id
                )
            list_of_ride_requests.append(ride_request_dto)
        return list_of_ride_requests

    def get_user_dtos(self, matched_persons_ids: List[int]):
        user_dtos_list = []
        if matched_persons_ids:
            user_objs = list(User.objects.filter(id__in=matched_persons_ids))
            for user_obj in user_objs:
                user_dto = UserDto(
                    user_id=user_obj.id,
                    user_name=user_obj.user_name,
                    mobile_number=user_obj.mobile_number
                    )
                user_dtos_list.append(user_dto)
        return user_dtos_list

    def get_matching_asset_requests_dto_with_flexible_timings(
        self,
        ride_share_to_datetime: datetime,
        ride_share_from_datetime: datetime,
        ride_share_source: str,ride_share_destination: str,
        limit: int,offset: int):
        matching_asset_request_objs = AssetTransportRequest.objects.filter(
            Q(from_datetime__gte=ride_share_from_datetime,
              from_datetime__lte=ride_share_to_datetime)|
            Q(to_datetime__lte=ride_share_to_datetime,
              to_datetime__gte=ride_share_from_datetime),
            source=ride_share_source,destination=ride_share_destination
            )[offset:limit]
        return self.get_list_of_asset_dtos_to_asset_request_objs(
            matching_asset_request_objs)

    def get_matching_asset_requests_dto_without_flexible_timings(
        self,
        ride_share_datetime: datetime,
        ride_share_source: str,ride_share_destination: str,
        limit: int,offset: int):

        matching_asset_request_objs = AssetTransportRequest.objects.filter(
            datetime=ride_share_datetime,
            source=ride_share_source,
            destination=ride_share_destination
            )[offset:limit]
        return self.get_list_of_asset_dtos_to_asset_request_objs(
            matching_asset_request_objs)

    def get_list_of_asset_dtos_to_asset_request_objs(self,
        matching_asset_request_objs):
        list_of_asset_requests=[]
        for request in matching_asset_request_objs:
            asset_request_dto = AssetRequestDto(
                user_id=request.user_id,
                source=request.source,
                destination=request.destination,
                is_flexible=request.is_flexible,
                datetime=str(request.datetime),
                from_datetime=str(request.from_datetime),
                to_datetime=str(request.to_datetime),
                no_of_assets=request.no_of_assets,
                deliver_person=request.deliver_person,
                asset_type=request.asset_type,
                sensitivity=request.sensitivity,
                accepted_person_id=request.accepted_person_id
                )
            list_of_asset_requests.append(asset_request_dto)
        return list_of_asset_requests

    def get_user_travel_info_shares_from_current_day(self, user_id: int):
        current_datetime= datetime.datetime.now()
        share_travel_info_objects=ShareTravelInfo.objects\
        .filter(Q(is_flexible=False,datetime__gt=current_datetime)|\
        Q(is_flexible=True,to_datetime__gt=current_datetime),user_id=user_id)

        return self.convert_share_travel_info_objects_to_list_of_dtos(
            share_travel_info_objects)

    def convert_share_travel_info_objects_to_list_of_dtos(self,
            share_travel_info_objects):
        list_of_share_travel_info_dtos=[]
        for travel_info_obj in share_travel_info_objects:
            list_of_share_travel_info_dtos.append(
                self.convert_share_travel_info_object_to_dto(travel_info_obj)
                )
        return list_of_share_travel_info_dtos

    def convert_share_travel_info_object_to_dto(self,travel_info_obj):
        share_travel_info_dto = ShareTravelInfoDto(
            user_id=travel_info_obj.user_id,
            source=travel_info_obj.source,
            destination=travel_info_obj.destination,
            is_flexible=travel_info_obj.is_flexible,
            datetime=travel_info_obj.datetime,
            from_datetime=travel_info_obj.from_datetime,
            to_datetime=travel_info_obj.to_datetime,
            medium=travel_info_obj.medium,
            assets_quantity=travel_info_obj.assets_quantity,
            )
        return share_travel_info_dto
