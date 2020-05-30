import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from lets_ride.interactors.get_my_asset_request_interactor import \
   GetMyAssetRequestsInteractor
from lets_ride.presenters.presenter_implementation \
    import PresenterImplementation
from lets_ride.storages.storage_implementation \
    import StorageImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    query_params=kwargs["request_query_params"]
    limit = query_params.limit
    offset = query_params.offset
    user_id = user.id

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetMyAssetRequestsInteractor(storage=storage, presenter=presenter)

    request_dict=interactor.get_my_asset_requests(
        offset =offset,
        limit=limit,
        user_id = user_id
        )
    response_data = json.dumps(request_dict)
    return HttpResponse(response_data, status=200)