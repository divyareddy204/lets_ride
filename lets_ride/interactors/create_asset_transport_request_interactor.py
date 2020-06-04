from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.exceptions.exceptions import InvalidPassword, \
    InvalidUserName, InvalidSource, InvalidDestination
from lets_ride.constants.enums import AssetType, SensitivityType

class CreateAssetTransportRequestInteractor:

    def __init__(self,storage: PostStorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def create_asset_transport_request(
        self,
        source: str,
        destination: str,
        is_flexible: bool,
        datetime: str,
        from_datetime: str,
        to_datetime: str,
        no_of_assets: int,
        asset_type: AssetType,
        sensitivity: SensitivityType,
        deliver_person: str,
        user_id: int
        ):

        self.storage.create_asset_transport_request(
            source=source,
            destination=destination ,
            is_flexible=is_flexible,
            datetime=datetime,
            from_datetime=from_datetime,
            to_datetime=to_datetime,
            no_of_assets=no_of_assets,
            asset_type=asset_type,
            sensitivity=sensitivity,
            deliver_person=deliver_person,
            user_id = user_id
            )
