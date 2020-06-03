import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from lets_ride.interactors.user_login_interactor import \
    UserLoginInteractor
from lets_ride.presenters.presenter_implementation \
    import PresenterImplementation
from lets_ride.storages.storage_implementation \
    import StorageImplementation
from .validator_class import ValidatorClass
from common.oauth2_storage import OAuth2SQLStorage

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs['request_data']
    mobile_number = request_data["mobile_number"]
    password = request_data["password"]

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    oauth_storage= OAuth2SQLStorage()
    interactor =UserLoginInteractor(storage=storage,
                                    presenter=presenter,
                                    oauth_storage=oauth_storage)

    access_token=interactor.user_login(
        password=password,
        mobile_number=mobile_number)
    
    response_data = json.dumps(access_token)
    return HttpResponse(response_data, status=200)