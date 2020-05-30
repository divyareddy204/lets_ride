from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
import datetime
class GetMyRideRequestsInteractor:
    
    def __init__(self, storage: PostStorageInterface,
                 presenter: PresenterInterface):
                     self.storage = storage
                     self.presenter = presenter
    
    def get_my_ride_requests(self, user_id: int):

        ride_requests_dto = self.storage.get_my_ride_requests_dto(
            user_id=user_id)

        ride_requests_dto_with_status=self._get_ride_request_with_status(
            self, ride_requests_dto)
        
        return self.presenter.get_my_ride_requests_response(
            my_ride_requests_dto = ride_requests_dto_with_status
            )
    
    def _get_ride_request_with_status(self, ride_requests_dto):
        for request in ride_requests_dto:
            if not request.flexible:
                if request.datetime>datetime.now():
                    status = "Expired"
            RideRequestWithStatusDto