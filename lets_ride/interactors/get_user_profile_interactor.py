from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.exceptions.exceptions import InvalidUserName


class GetUserProfileInteractor():
    
    def __init__(self, storage: PostStorageInterface,
                 presenter: PresenterInterface):
                     self.storage = storage
                     self.presenter = presenter
    
    def get_user_profile(self, user_name: str):
        
        try:
            self.storage.validate_user_name(user_name=user_name)
        except InvalidUserName:
            self.presenter.raise_exception_for_invalid_user()
            return
        user_dto = self.storage.get_user_profile(user_name=user_name)
        
        return self.presenter.get_user_profile_response(user_dto=user_dto)
