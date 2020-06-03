import pytest
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
user_auth_dto={
        "user_id": 1,
        "access_token" : "fyiduasf",
        "refresh_token" : "fhjskfjaisk",
        "expires_in" : "2020, 12, 5"
            }

@patch.object(OAuthUserAuthTokensService, "create_user_auth_tokens",
              return_value=user_auth_dto)
def validate_user(create_user_auth_tokens):

    #Arrange
    mobile_number = "0932825493"
    user_name = "user1"
    password = "password"
    user_id = 1
    expected_output = user_auth_dto
    storage = create_autospec(PostStorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = create_autospec(OAuth2SQLStorage)
    service = create_autospec(OAuthUserAuthTokensService(oauth2_storage=oauth_storage))
    interactor = CreateUserInteractor(
        storage=storage,
        presenter=presenter,
        oauth_storage=oauth_storage
        )

    presenter.create_user_response.return_value = {
        'user_id': 1,
        'access_token': 'fyiduasf',
        'refresh_token': 'fhjskfjaisk',
        'expires_in': '2020, 12, 5'}
    storage.validate_user_name.return_value = expected_output
    service.create_user_auth_tokens.return_value = user_auth_dto
    #Act
    response = interactor.create_user(
        user_name=user_name,
        mobile_number=mobile_number,
        password=password
        )

    #Assert
    print(response)
    print("**************************")
    print(expected_output)
    storage.validate_user_name.assert_called_once_with(
       user_name=user_name)
    presenter.create_user_response.assert_called_once_with(
        user_access_dto=user_auth_dto)
    service.create_user_auth_tokens.assert_called_once_with(user_id=user_id)
    assert response == expected_output

@patch.object(OAuthUserAuthTokensService, "create_user_auth_tokens",
              return_value=user_auth_dto)
def validate_password_returns_user_id(oauth_user_auth_tokens_service):

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
    interactor = CreateUserInteractor(
        storage=storage,
        presenter=presenter,
        oauth_storage=oauth_storage
        )

    storage.validate_password_for_user.return_value = user_id
    presenter.create_user_response.return_value = expected_output
    service.create_user_auth_tokens.return_value = user_auth_dto
    #Act
    response = interactor.create_user(
        mobile_number=mobile_number,
        user_name=user_name,
        password=password
        )
    print(response)
    print("**************************")
    print(expected_output)
    #Assert
    storage.validate_password_for_user.assert_called_once_with(
       user_name=user_name,
       password=password)
    presenter.create_user_response.assert_called_once_with(
        user_access_dto=user_auth_dto)
    service.create_user_auth_tokens.assert_called_once_with(user_id=user_id)
    assert response == expected_output

