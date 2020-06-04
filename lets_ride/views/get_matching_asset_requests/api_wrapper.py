import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from lets_ride.interactors.get_matching_asset_requests_interactor import \
   GetMatchingAssetRequests
from lets_ride.presenters.presenter_implementation \
    import PresenterImplementation
from lets_ride.storages.storage_implementation \
    import StorageImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    query_params=kwargs["request_query_params"]
    print("query_params_limit*******************",query_params.limit)
    print("query_params_offset*******************",query_params.offset)
    limit = query_params.limit
    offset = query_params.offset

    user_id = user.id

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetMatchingAssetRequests(storage=storage, presenter=presenter)

    request_dict=interactor.get_matching_asset_requests(
        user_id=user_id,
        offset=offset,
        limit=limit
    )
    #print(request_dict)

    response_data = json.dumps(request_dict)
    return HttpResponse(response_data, status=200)
