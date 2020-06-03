from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface

class GetMatchingAssetRequests:
    
    def __init__(self, storage=PostStorageInterface, presenter=PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_matching_ride_requests(self, user_id: int):
        matching_requests=self.storage.get_matching_asset_requests_dto(
            user_id=user_id)
        
        matched_persons_ids = [request.user_id for request in matching_requests]
        matched_user_dtos=self.storage.get_user_dtos(matched_persons_ids)
        
        return self.presenter.get_response_for_matching_ride_requests(
            matchig_ride_requests=matching_requests)
