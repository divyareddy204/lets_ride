from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface


class CreateRideRequestInteractor:

    def __init__(self,storage: PostStorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def create_ride_request(self,
        source: str,
        destination: str,
        is_flexible: bool,
        datetime: str,
        from_datetime: str,
        to_datetime: str,
        no_of_seats: int,
        luggage_quantity: int,
        user_id: int):

        self.storage.create_ride_request(
            source=source,
            destination=destination ,
            is_flexible=is_flexible,
            datetime=datetime,
            from_datetime=from_datetime,
            to_datetime=to_datetime,
            no_of_seats=no_of_seats,
            luggage_quantity=luggage_quantity,
            user_id = user_id
        )
