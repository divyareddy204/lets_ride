
from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.exceptions.exceptions import InvalidPassword, \
    InvalidUserName
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService

class CreateUserInteractor:

    def __init__(self,storage: PostStorageInterface,
                 presenter: PresenterInterface,
                 oauth_storage: OAuth2SQLStorage()):
        self.storage = storage
        self.presenter = presenter
        self.oauth_storage = oauth_storage

    def create_user(self, user_name: str, mobile_number: str, password: str):

        try:
            self.storage.validate_user_name(user_name=user_name)
        except InvalidUserName:
            self.presenter.raise_exception_for_invalid_user()
            return
        try:
            user_id=self.storage.validate_password_for_user(
                user_name=user_name,
                password=password
                )
        except  InvalidPassword:
            self.presenter.raise_exception_for_invalid_password()
            return

        service = OAuthUserAuthTokensService(oauth2_storage=self.oauth_storage)
        user_access_dto=service.create_user_auth_tokens(user_id=user_id)
        print(user_access_dto)
        return self.presenter.create_user_response(user_access_dto=user_access_dto)
