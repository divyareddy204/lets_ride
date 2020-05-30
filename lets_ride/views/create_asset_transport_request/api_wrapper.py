import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from lets_ride.interactors.create_asset_transport_request_interactor import \
    CreateAssetTransportRequestInteractor
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
    flexible = request_data["flexible"]
    from_datetime = request_data["from_datetime"]
    to_datetime = request_data["to_datetime"]
    datetime = request_data["datetime"]
    no_of_assets =request_data["no_of_assets"]
    asset_type = request_data["asset_type"]
    sensitivity = request_data["sensitivity"]
    deliver_person  = request_data["deliver_person"]
    user_id = user.id

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = CreateAssetTransportRequestInteractor(
        storage=storage, presenter=presenter)

    interactor.create_asset_transport_request(
        source=source,
        destination=destination ,
        flexible=flexible,
        datetime=datetime,
        from_datetime=from_datetime,
        to_datetime=to_datetime,
        asset_type=asset_type,
        sensitivity=sensitivity,
        no_of_assets=no_of_assets,
        deliver_person=deliver_person,
        user_id = user_id
        )

    return HttpResponse(status=201)