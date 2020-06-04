import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from lets_ride.interactors.create_ride_request_interactor import \
    CreateRideRequestInteractor
from lets_ride.presenters.presenter_implementation \
    import PresenterImplementation
from lets_ride.storages.storage_implementation \
    import StorageImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    request_data = kwargs['request_data']
    source = request_data["source"]
    destination = request_data["destination"]
    is_flexible = request_data["is_flexible"]
    from_datetime = request_data["from_datetime"]
    to_datetime = request_data["to_datetime"]
    datetime = request_data["datetime"]
    no_of_seats =request_data["no_of_seats"]
    luggage_quantity = request_data["luggage_quantity"]
    user_id = user.id

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateRideRequestInteractor(storage=storage, presenter=presenter)

    interactor.create_ride_request(
        source=source,
        destination=destination ,
        is_flexible=is_flexible,
        datetime=datetime,
        from_datetime=from_datetime,
        to_datetime=to_datetime,
        no_of_seats=no_of_seats,
        luggage_quantity=luggage_quantity,
        user_id = user_id
        )
    return HttpResponse(status=201)