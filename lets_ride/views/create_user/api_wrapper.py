import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from fb_post_v2.interactors.create_user_interactor import \
    CreateUserInteractor
from lets_ride.presenters.presenter_implementation \
    import PresenterImplementation
from lets_ride.storages.storage_implementation \
    import StorageImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs['request_data']
    mobile_number = request_data.mobile_number
    user_name = request_data.user_name
    password = request_data.password


    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateUserInteractor(storage=storage, presenter=presenter)

    interactor.create_post(
        user_name = user_name,
        password=password,
        mobile_number=mobile_number)

    return HttpResponse(status=201)