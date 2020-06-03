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
        #sort_by: datetime,
        #order: str
        ):
        if status:
            ride_requests_dtos = self.storage.\
            get_my_ride_requests_dto_filter_by_status(
                user_id=user_id,
                limit=limit,
                offset=offset,
                status=status)
        else:
            ride_requests_dtos = self.storage.get_my_ride_requests_dto(
                user_id=user_id,
                limit=limit,
                offset=offset)
        
        list_of_accepted_persons_ids = []
        for request in ride_requests_dtos:
            if request.accepted_person_id:
                list_of_accepted_persons_ids.append(request.accepted_person_id)

        user_dtos = self.storage.get_accepted_persons_dtos(
            list_of_accepted_persons_ids)

        list_of_ride_requests=self._get_ride_request_with_status(
            ride_requests_dtos)
        total_requests = self.storage.get_total_requests()
        
        print("**************** :",list_of_ride_requests)
        
        all_ride_request_details = self._get_all_ride_request_details(
            total_requests=total_requests,
            limit=limit,
            offset=offset,
            list_of_ride_requests=list_of_ride_requests)
        
        print("my_ride_request_dto:", all_ride_request_details)
        print(self.presenter.get_my_ride_requests_response(
            my_ride_request_dto = all_ride_request_details, user_dtos=user_dtos
            ))
        return self.presenter.get_my_ride_requests_response(
            my_ride_request_dto = all_ride_request_details, user_dtos=user_dtos)

    def _get_ride_request_with_status(self, ride_request_dtos):
        list_of_ride_requests=[]
        for request in ride_request_dtos:
            print("**************",request.flexible)
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
        print(request.datetime[:-6])
        print("**************************")
        if datetime.strptime(request.datetime[:-6],"%Y-%m-%d %H:%M:%S")>datetime.now():
            status =StatusValue.Expired.value
        else:
            status = StatusValue.Pending.value
        return status
        
    def check_status_if_flexible_is_true(self,request):
        if datetime.strptime(request.datetime[:-6],"%Y-%m-%d %H:%M:%S")>datetime.now():
            status =StatusValue.Expired.value
        else:
            status = StatusValue.Pending.value
        return status
        
        
    def _get_all_ride_request_details(self,
        total_requests,limit,offset,list_of_ride_requests):
            
            request= MyRideRequestsDto(
                total_requests=total_requests,
                request_dtos=list_of_ride_requests,
                limit=limit,
                offset=offset
                )
            print("request************************",request)
            return request
































































