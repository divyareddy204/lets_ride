from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.interactors.storages.dtos \
    import RideRequestWithStatusDto, MyRideRequestsDto
from datetime import datetime
import pytz
from lets_ride.constants.enums import StatusValue

class GetMyRideRequestsInteractor:
    
    def __init__(self, storage: PostStorageInterface,
                 presenter: PresenterInterface):
                     self.storage = storage
                     self.presenter = presenter
    
    def get_my_ride_requests(self,
        user_id: int,
        limit: int,
        offset: int,
        status: str,
        sort_by: str,
        order: str
        ):
        print("interactor: ",status)
        
        if status == StatusValue.Expired.value:
            print("interactor: ",status)
            ride_requests_dtos = self.storage.\
            get_my_ride_requests_dto_filter_by_expired_status_value(
                user_id=user_id,
                limit=limit,
                offset=offset)
            print("interactor:-----",ride_requests_dtos)

        elif status == StatusValue.Pending.value:
            ride_requests_dtos = self.storage.\
            get_my_ride_requests_dto_filter_by_active_status_value(
                user_id=user_id,
                limit=limit,
                offset=offset)

        elif status==StatusValue.Confirmed.value:
            ride_requests_dtos = self.storage.\
            get_my_ride_requests_dto_filter_by_confirmed_status_value(
                user_id=user_id,
                limit=limit,
                offset=offset)
        elif order=="ASC":
            ride_requests_dtos = self.storage.\
            get_my_ride_requests_dto_sort_by_ascending_order(
                user_id=user_id,
                limit=limit,
                offset=offset,
                sort_by=sort_by)

            #print("interactor:-----",ride_requests_dtos)
        elif order=="DESC":
            ride_requests_dtos = self.storage.\
            get_my_ride_requests_dto_sort_by_descending_order(
                user_id=user_id,
                limit=limit,
                offset=offset,
                sort_by=sort_by)

        else:
            print("interactor:-----fouthfunction")
            ride_requests_dtos = self.storage.get_my_ride_requests_dto(
                user_id=user_id,
                limit=limit,
                offset=offset)
        
        list_of_accepted_persons_ids = []
        for request in ride_requests_dtos:
            if request.accepted_person_id:
                list_of_accepted_persons_ids.append(request.accepted_person_id)
        print("accepted_person_id:****",list_of_accepted_persons_ids)
        user_dtos = self.storage.get_accepted_persons_dtos(
            list_of_accepted_persons_ids)

        list_of_ride_requests=self._get_ride_request_with_status(
            ride_requests_dtos)
        total_requests = self.storage.get_total_requests()
        
        all_ride_request_details = self._get_all_ride_request_details(
            total_requests=total_requests,
            limit=limit,
            offset=offset,
            list_of_ride_requests=list_of_ride_requests)
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("my_ride_request_dto:", all_ride_request_details)
        return self.presenter.get_my_ride_requests_response(
            my_ride_request_dto = all_ride_request_details, user_dtos=user_dtos)

    def _get_ride_request_with_status(self, ride_request_dtos):
        list_of_ride_requests=[]
        for request in ride_request_dtos:
            if not request.flexible:
                status=self.check_status_if_flexible_is_false(request)
            else:
                status = self.check_status_if_flexible_is_true(request)
            status=self.check_accepted_person_exists_for_the_request(request)
            
            list_of_ride_requests.append(
                RideRequestWithStatusDto(ride_request_dto=request,
                                         status=status)
                )
        return list_of_ride_requests

    def check_accepted_person_exists_for_the_request(self, request):
        if request.accepted_person_id:
            status = StatusValue.Confirmed.value
        else:
            status = StatusValue.Pending.value
        return status
        
    def check_status_if_flexible_is_false(self,request):
        if request.datetime.replace(tzinfo=None)>datetime.now():
            status =StatusValue.Expired.value
        else:
            status = StatusValue.Pending.value
        return status
        
    def check_status_if_flexible_is_true(self,request):
        if request.to_datetime.replace(tzinfo=None)>datetime.now():
            status =StatusValue.Expired.value
        else:
            status = StatusValue.Pending.value
        return status
        
        
    def _get_all_ride_request_details(self,
        total_requests,limit,offset,list_of_ride_requests):
            
            print("*"*180)
            print("atlast")
            print(list_of_ride_requests)
            print("*"*180)
            
            request= MyRideRequestsDto(
                total_requests=total_requests,
                request_dtos=list_of_ride_requests,
                limit=limit,
                offset=offset
                )
            print("request", request)
            return request