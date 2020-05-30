from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.interactors.storages.dtos \
    import RideRequestWithStatusDto, MyRideRequestsDto
from datetime import datetime
import pytz
class GetMyRideRequestsInteractor:
    
    def __init__(self, storage: PostStorageInterface,
                 presenter: PresenterInterface):
                     self.storage = storage
                     self.presenter = presenter
    
    def get_my_ride_requests(self, user_id: int, limit: int, offset: int):
    
        ride_requests_dtos = self.storage.get_my_ride_requests_dto(
            user_id=user_id, limit=limit, offset=offset)
        
        list_of_ride_requests=self._get_ride_request_with_status(
            ride_requests_dtos)
        total_requests = self.storage.get_total_requests()
        #print("********",list_of_ride_requests)
        all_ride_request_details = self._get_all_ride_request_details(
            total_requests=total_requests,
            limit=limit,
            offset=offset,
            list_of_ride_requests=list_of_ride_requests)
        
        #print(all_ride_request_details)
        return self.presenter.get_my_ride_requests_response(
            my_ride_request_dto = all_ride_request_details
            )

    def _get_ride_request_with_status(self, ride_request_dtos):
        list_of_ride_requests=[]
        for request in ride_request_dtos:
            if not request.flexible:
                if str(request.datetime)>str(pytz.utc.localize(datetime.now())):
                    status = "Expired"
                else:
                    status = "Pending"
            elif str(request.to_datetime)>str(pytz.utc.localize(datetime.now())):
                status = "Expired"
            else:
                status = "Pending"
            if request.accepted_person_id:
                status = "Confirmed"
            
            list_of_ride_requests.append(
                RideRequestWithStatusDto(ride_request_dto=request,
                                         status=status)
                )
        return list_of_ride_requests
    
    def _get_all_ride_request_details(self,
        total_requests,limit,offset,list_of_ride_requests):
            
            return MyRideRequestsDto(
                total_requests=total_requests,
                request_dtos=list_of_ride_requests,
                limit=limit,
                offset=offset
                )