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

        limit_value_negative =  limit<0
        offset_value_negative = offset<0

        if limit_value_negative:
            self.presenter.raise_exception_for_invalid_limit()
        if offset_value_negative:
            self.presenter.raise_exception_for_invalid_offset()


        share_ride_dtos=self.storage.get_user_ride_shares_from_current_day(
            user_id=user_id)

        share_traval_info_dtos=self.\
        storage.get_user_travel_info_shares_from_current_day(user_id=user_id)

        list_of_matching_asset_request_dtos=[]
        for share_object_dto in share_ride_dtos:
            if share_object_dto.is_flexible:
                matching_asset_request_dtos=self.\
                storage.get_matching_asset_requests_dto_with_flexible_timings(
                    ride_share_to_datetime=share_object_dto.\
                    to_datetime+timedelta(days=1),
                    ride_share_from_datetime=share_object_dto.\
                    from_datetime-timedelta(days=1),
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

        for share_travel_info_dto in share_traval_info_dtos:
            if share_travel_info_dto.is_flexible:
                matching_asset_request_dtos=self.\
                storage.get_matching_asset_requests_dto_with_flexible_timings(
                    ride_share_to_datetime=share_travel_info_dto.\
                    to_datetime+timedelta(days=1),
                    ride_share_from_datetime=share_travel_info_dto.\
                    from_datetime-timedelta(days=1),
                    ride_share_source=share_travel_info_dto.source,
                    ride_share_destination=share_travel_info_dto.destination,
                    limit=limit,
                    offset=offset)
            else:
                matching_asset_request_dtos=self.\
                storage.get_matching_asset_requests_dto_without_flexible_timings(
                    ride_share_datetime=share_travel_info_dto.datetime,
                    ride_share_source=share_travel_info_dto.source,
                    ride_share_destination=share_travel_info_dto.destination,
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
            matched_user_dtos=matched_user_dtos,limit=limit,offset=offset)
