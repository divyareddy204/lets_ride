from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.interactors.storages.dtos \
    import AssetRequestWithStatusDto, MyAssetRequestsDto
from datetime import datetime
import pytz
from lets_ride.constants.enums import StatusValue
status = StatusValue.Pending.value
class GetMyAssetRequestsInteractor:
    
    def __init__(self, storage: PostStorageInterface,
                 presenter: PresenterInterface):
                     self.storage = storage
                     self.presenter = presenter
    
    
    def get_my_asset_requests(self, user_id: int,
        limit: int,
        offset: int,
        status: str,
        sort_by: datetime,
        order: str):

        if status == StatusValue.Expired.value:
            print("interactor: ",status)
            asset_requests_dtos = self.storage.\
            get_my_asset_requests_dto_filter_by_expired_status_value(
                user_id=user_id,
                limit=limit,
                offset=offset)
            print("interactor:-----",asset_requests_dtos)

        elif status == StatusValue.Pending.value:
            asset_requests_dtos = self.storage.\
            get_my_asset_requests_dto_filter_by_active_status_value(
                user_id=user_id,
                limit=limit,
                offset=offset)

        elif status==StatusValue.Confirmed.value:
            asset_requests_dtos = self.storage.\
            get_my_asset_requests_dto_filter_by_confirmed_status_value(
                user_id=user_id,
                limit=limit,
                offset=offset)

        elif order=="ASC":
            asset_requests_dtos = self.storage.\
            get_my_asset_requests_dto_sort_by_ascending_order(
                user_id=user_id,
                limit=limit,
                offset=offset,
                sort_by=sort_by)

        elif order=="DESC":
            asset_requests_dtos = self.storage.\
            get_my_asset_requests_dto_sort_by_descending_order(
                user_id=user_id,
                limit=limit,
                offset=offset,
                sort_by=sort_by)
        else:
            print("interactor:-----fouthfunction")
            asset_requests_dtos = self.storage.get_my_asset_requests_dto(
                user_id=user_id,
                limit=limit,
                offset=offset)
        
        list_of_accepted_persons_ids = []
        for request in asset_requests_dtos:
            if request.accepted_person_id:
                list_of_accepted_persons_ids.append(request.accepted_person_id)
        user_dtos = self.storage.get_accepted_persons_dtos(
            list_of_accepted_persons_ids)

        list_of_asset_requests=self._get_asset_request_with_status(
            asset_requests_dtos)
        total_requests = self.storage.get_total_requests()
        #print("********",list_of_asset_requests)
        all_asset_request_details = self._get_all_asset_request_details(
            total_requests=total_requests,
            limit=limit,
            offset=offset,
            list_of_asset_requests=list_of_asset_requests)
        
        #print(all_asset_request_details)
        return self.presenter.get_my_asset_requests_response(
            my_asset_request_dto = all_asset_request_details, user_dtos=user_dtos
            )

    def _get_asset_request_with_status(self, asset_request_dtos):
        list_of_asset_requests=[]
        for request in asset_request_dtos:
            if not request.flexible:
                status=self.check_status_if_flexible_is_false(request)
            else:
                status = self.check_status_if_flexible_is_true(request)
            status=self.check_accepted_person_exists_for_the_request(request)
            
            list_of_asset_requests.append(
                AssetRequestWithStatusDto(asset_request_dto=request,
                                         status=status)
                )
        return list_of_asset_requests

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
        
        
    def _get_all_asset_request_details(self,
        total_requests,limit,offset,list_of_asset_requests):
            
            request= MyAssetRequestsDto(
                total_requests=total_requests,
                request_dtos=list_of_asset_requests,
                limit=limit,
                offset=offset
                )
            return request