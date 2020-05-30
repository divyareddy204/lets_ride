
from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface

class CreateUserInteractor:
    
    def __init__(self,storage: PostStorageInterface,
                 presenter:PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def create_user(self, user_name: str, mobile_number: str, password: str):
        
        = self.storage.create_user(
            mobile_number=mobile_number,
            user_name=user_name,
            password=password
            )
        return self.presenter.create_user_response(access_token=access_token)
    