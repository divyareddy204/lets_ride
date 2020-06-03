
from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.exceptions.exceptions import InvalidPassword, \
    InvalidMobileNumber
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService

class UserLoginInteractor:

    def __init__(self,storage: PostStorageInterface,
                 presenter: PresenterInterface,
                 oauth_storage: OAuth2SQLStorage()):
        self.storage = storage
        self.presenter = presenter
        self.oauth_storage = oauth_storage

    def user_login(self, mobile_number: str, password: str):
        try:
            self.storage.validate_mobile_number(mobile_number=mobile_number)
        except InvalidMobileNumber:
            self.presenter.raise_exception_for_invalid_mobile_number()
            return
        try:
            user_id=self.storage.validate_password_for_user(
                mobile_number=mobile_number,
                password=password
                )
        except  InvalidPassword:
            self.presenter.raise_exception_for_invalid_password()
            return
        
        service = OAuthUserAuthTokensService(oauth2_storage=self.oauth_storage)
        user_access_dto=service.create_user_auth_tokens(user_id=user_id)
        print(user_access_dto)
        return self.presenter.user_login_response(user_access_token_dto=user_access_dto)
