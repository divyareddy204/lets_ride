from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.interactors.storages.dtos \
    import AssetRequestWithStatusDto, MyAssetRequestsDto
from datetime import datetime
import pytz
class GetMyAssetRequestsInteractor:
    
    def __init__(self, storage: PostStorageInterface,
                 presenter: PresenterInterface):
                     self.storage = storage
                     self.presenter = presenter
    
    def get_my_asset_requests(self, user_id: int, limit: int, offset: int):
    
        asset_requests_dtos = self.storage.get_my_asset_requests_dto(
            user_id=user_id, limit=limit, offset=offset)
        
        list_of_asset_requests=self._get_asset_request_with_status(
            asset_requests_dtos)
        total_requests = self.storage.get_total_asset_requests()
        #print("********",list_of_asset_requests)
        all_asset_request_details = self._get_all_asset_request_details(
            total_requests=total_requests,
            limit=limit,
            offset=offset,
            list_of_asset_requests=list_of_asset_requests)
        
        #print(all_asset_request_details)
        return self.presenter.get_my_asset_requests_response(
            my_asset_request_dto = all_asset_request_details
            )

    def _get_asset_request_with_status(self, asset_request_dtos):
        list_of_asset_requests=[]
        for request in asset_request_dtos:
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
            
            list_of_asset_requests.append(
                AssetRequestWithStatusDto(asset_request_dto=request,
                                         status=status)
                )
        return list_of_asset_requests
    
    def _get_all_asset_request_details(self,
        total_requests,limit,offset,list_of_asset_requests):
            
            return MyAssetRequestsDto(
                total_requests=total_requests,
                request_dtos=list_of_asset_requests,
                limit=limit,
                offset=offset
                )