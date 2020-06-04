from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface


class CreateShareRideInteractor:

    def __init__(self,storage: PostStorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def create_share_ride(self,
        source: str,
        destination: str,
        is_flexible: bool,
        datetime: str,
        from_datetime: str,
        to_datetime: str,
        no_of_seats_available: int,
        assets_quantity: int,
        user_id: int):

        self.storage.create_share_ride(
            source=source,
            destination=destination ,
            is_flexible=is_flexible,
            datetime=datetime,
            from_datetime=from_datetime,
            to_datetime=to_datetime,
            no_of_seats_available=no_of_seats_available,
            assets_quantity=assets_quantity,
            user_id = user_id
        )
