from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.exceptions.exceptions import InvalidS,

class CreateRideRequestInteractor:

    def __init__(self,storage: PostStorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def create_ride_request(self,
        source: str,
        destination: str,
        flexible: bool,
        datetime: str,
        from_datetime: str,
        to_datetime: str,
        no_of_seats: int,
        luggage_quantity: int):
        try:
            self.storage.validate_source(source=source)
        except InvalidSource:
            raise InvalidSource
            
        
            self.storage.validate_source(destination=destination)
            source=source,
            destination=destination ,
            flexible=flexible,
            datetime=datetime,
            from_datetime=from_datetime,
            to_datetime=to_datetime,
            no_of_seats=no_of_seats,
            luggage_quantity=luggage_quantity
        )
