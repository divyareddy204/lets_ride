from unittest.mock import create_autospec, patch
from lets_ride.interactors.create_user_interactor import CreateUserInteractor
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
import common
from common.dtos import UserAuthTokensDTO
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
@pytest.fixture
UserAuthTokensDTO(
@patch.object(OAuthUserAuthTokensService, "oauth_user_auth_tokens_service", return_value=UserAuthTokensDTO)
        access_token = "fyiduasf",
        refresh_token = "fhjskfjaisk",
        expires_in = "2020, 12, 5"
        )

@patch.object(OAuthUserAuthTokensService, "oauth_user_auth_tokens_service", return_value=UserAuthTokensDTO)
def test_create_user_returns_user_id(oauth_user_auth_tokens_service):
    
    #Arrange
    mobile_number = "0932825493"
    user_name = "user1"
    password = "password"
    user_id = 1
    expected_output = {"user_id": user_id}
    storage = create_autospec(PostStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = create_autospec(OAuth2SQLStorage)
    service = create_autospec(OAuthUserAuthTokensService(oauth2_storage=oauth_storage))
    #@mock.patch("os.listdir", mock.MagicMock(return_value="test1"))
    interactor = CreateUserInteractor(
        storage=storage,
        presenter=presenter,
        oauth_storage=oauth_storage
        )
    
    storage.create_user.return_value = user_id
    presenter.create_user_response.return_value = expected_output
    service.create_user_auth_tokens.return_value =
    #Act
    response = interactor.create_user(
        mobile_number=mobile_number,
        user_name=user_name,
        password=password
        )

    #Assert
    storage.create_user.assert_called_once_with(
        mobile_number=mobile_number,
        user_name=user_name,
        password=password)
    presenter.create_user_response.assert_called_once_with(
        )
    service.create_user_auth_tokens.assert_called_once_with(user_id=user_id)
    assert response == expected_output
    