from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.constants.enums import MediumType

class CreateShareTravelInfoInteractor:

    def __init__(self,storage: PostStorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def create_share_travel_info(self,
        source: str,
        destination: str,
        flexible: bool,
        datetime: str,
        from_datetime: str,
        to_datetime: str,
        medium: MediumType,
        assets_quantity: int,
        user_id: int):

        self.storage.create_share_travel_info(
            source=source,
            destination=destination ,
            flexible=flexible,
            datetime=datetime,
            from_datetime=from_datetime,
            to_datetime=to_datetime,
            medium=medium,
            assets_quantity=assets_quantity,
            user_id = user_id
        )
