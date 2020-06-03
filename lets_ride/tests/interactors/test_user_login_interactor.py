import pytest
from unittest.mock import create_autospec, patch
from django_swagger_utils.drf_server.exceptions import NotFound
from lets_ride.interactors.user_login_interactor import UserLoginInteractor
from lets_ride.interactors.presenters.presenter_interface \
    import PresenterInterface
from lets_ride.interactors.storages.post_storage_interface \
    import PostStorageInterface
from lets_ride.exceptions.exceptions import InvalidMobileNumber
from common.dtos import UserAuthTokensDTO
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
user_auth_dto={
        "user_id": 1,
        "access_token" : "fyiduasf",
        "refresh_token" : "fhjskfjaisk",
        "expires_in" : "2020, 12, 5"
            }

@patch.object(OAuthUserAuthTokensService, "create_user_auth_tokens",
              return_value=user_auth_dto)
def test_user_login_given_valid_user_name(create_user_auth_tokens):

    #Arrange
    mobile_number = "0932825493"
    password = "password"
    user_id = 1
    expected_output = user_auth_dto
    storage = create_autospec(PostStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = create_autospec(OAuth2SQLStorage)
    service = create_autospec(OAuthUserAuthTokensService(oauth2_storage=oauth_storage))
    interactor = UserLoginInteractor(
        storage=storage,
        presenter=presenter,
        oauth_storage=oauth_storage
        )

    presenter.user_login_response.return_value = {
        'user_id': 1,
        'access_token': 'fyiduasf',
        'refresh_token': 'fhjskfjaisk',
        'expires_in': '2020, 12, 5'}
    storage.validate_mobile_number.return_value = expected_output
    service.create_user_auth_tokens.return_value = user_auth_dto
    #Act
    response = interactor.user_login(
        mobile_number=mobile_number,
        password=password
        )

    #Assert
    print(response)
    print(expected_output)
    storage.validate_mobile_number.assert_called_once_with(
       mobile_number=mobile_number)
    presenter.user_login_response.assert_called_once_with(
        user_access_token_dto=user_auth_dto)
    service.create_user_auth_tokens.assert_called_once_with(user_id=user_id)
    assert response == expected_output


@patch.object(OAuthUserAuthTokensService, "create_user_auth_tokens",
              return_value=user_auth_dto)
def test_user_login_given_invalid_mobile_number(create_user_auth_tokens):

    #Arrange
    mobile_number = "0932825493"
    password = "password"
    storage = create_autospec(PostStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = create_autospec(OAuth2SQLStorage)
    service = create_autospec(OAuthUserAuthTokensService(oauth2_storage=oauth_storage))
    interactor = UserLoginInteractor(
        storage=storage,
        presenter=presenter,
        oauth_storage=oauth_storage
        )
    storage.validate_mobile_number.side_effect = InvalidMobileNumber
    presenter.raise_exception_for_invalid_mobile_number.side_effect = NotFound
    #Act
    with pytest.raises(NotFound):
        interactor.user_login(
            mobile_number=mobile_number,
            password=password
            )

    #Assert
    storage.validate_mobile_number.assert_called_once_with(
       mobile_number=mobile_number)
    presenter.raise_exception_for_invalid_mobile_number.assert_called_once_with()

@patch.object(OAuthUserAuthTokensService, "create_user_auth_tokens",
              return_value=user_auth_dto)
def test_validate_password_returns_user_id(create_user_auth_tokens):

    #Arrange
    mobile_number = "0932825493"
    password = "password"
    user_id = 1
    expected_output = {"user_id": user_id}
    storage = create_autospec(PostStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = create_autospec(OAuth2SQLStorage)
    service = create_autospec(OAuthUserAuthTokensService(oauth2_storage=oauth_storage))
    interactor = UserLoginInteractor(
        storage=storage,
        presenter=presenter,
        oauth_storage=oauth_storage
        )

    storage.validate_password_for_user.return_value = user_id
    presenter.user_login_response.return_value = expected_output
    service.create_user_auth_tokens.return_value = user_auth_dto
    #Act
    response = interactor.user_login(
        mobile_number=mobile_number,
        password=password
        )

    #Assert
    storage.validate_password_for_user.assert_called_once_with(
       mobile_number=mobile_number,
       password=password)
    presenter.user_login_response.assert_called_once_with(
        user_access_token_dto=user_auth_dto)
    service.create_user_auth_tokens.assert_called_once_with(user_id=user_id)
    assert response == expected_output

