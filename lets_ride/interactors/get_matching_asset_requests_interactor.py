from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from datetime import timedelta
class GetMatchingAssetRequests:
    
    def __init__(self, storage=PostStorageInterface, presenter=PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_matching_asset_requests(self,
        user_id: int,
        offset: int,
        limit: int):
    
        share_object_dtos=self.storage.get_user_ride_shares_from_current_day(user_id=user_id)
        
        list_of_matching_asset_request_dtos=[]
        for share_object_dto in share_object_dtos:
            if share_object_dto.flexible:
                matching_asset_request_dtos=self.\
                storage.get_matching_asset_requests_dto_with_flexible_timings(
                    ride_share_to_datetime=share_object_dto.to_datetime+timedelta(days=1),
                    ride_share_from_datetime=share_object_dto.from_datetime-timedelta(days=1),
                    ride_share_source=share_object_dto.source,
                    ride_share_destination=share_object_dto.destination,
                    limit=limit,
                    offset=offset)
            else:
                matching_asset_request_dtos=self.\
                storage.get_matching_asset_requests_dto_without_flexible_timings(
                    ride_share_datetime=share_object_dto.datetime,
                    ride_share_source=share_object_dto.source,
                    ride_share_destination=share_object_dto.destination,
                    limit=limit,
                    offset=offset)
            list_of_matching_asset_request_dtos=[request for request 
            in matching_asset_request_dtos]
        
        print("*"*100)
        print("asset_requests", list_of_matching_asset_request_dtos)
        matched_persons_ids = [request.user_id for request in
        list_of_matching_asset_request_dtos]
        matched_user_dtos=self.storage.get_user_dtos(matched_persons_ids)
        
        return self.presenter.get_response_for_matching_asset_requests(
            matching_asset_requests=list_of_matching_asset_request_dtos,
            matched_user_dtos=matched_user_dtos)
