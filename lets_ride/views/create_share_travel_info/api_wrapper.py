import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from lets_ride.interactors.create_share_travel_info_interactor import \
    CreateShareTravelInfoInteractor
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
    medium = request_data["medium"]
    assets_quantity = request_data["assets_quantity"]
    user_id = user.id

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateShareTravelInfoInteractor(
        storage=storage, presenter=presenter)

    interactor.create_share_travel_info(
        source=source,
        destination=destination ,
        is_flexible=is_flexible,
        datetime=datetime,
        from_datetime=from_datetime,
        to_datetime=to_datetime,
        medium=medium,
        assets_quantity=assets_quantity,
        user_id = user_id
        )
    return HttpResponse(status=201)