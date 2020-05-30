
from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService

class CreateUserInteractor:

    def __init__(self,storage: PostStorageInterface,
                 presenter:PresenterInterface,
                 oauth_service = OAuthUserAuthTokensService):
        self.storage = storage
        self.presenter = presenter
    def create_user(self):
    
    def create_user(self, user_name: str, mobile_number: str, password: str):
        try:
            self.storage.validate_user(user_name)
        except:
            self.presenter.raise_exception_for_invalid_user()
            return
        try:
            self.storage.validate_password_for_user(
                mobile_number=mobile_number,
                user_name=user_name,
                password=password
                )
        except:
            self.presenter.raise_exception_for_invalid_password()
            return
        
        user_access_dto=self.oauth_service.create_user_auth_tokens(user_id=user_id)
        return self.presenter.create_user_response(user_access_dto=user_access_dto)

