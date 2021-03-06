import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from lets_ride.interactors.get_my_ride_requests_interactor import \
   GetMyRideRequestsInteractor
from lets_ride.presenters.presenter_implementation \
    import PresenterImplementation
from lets_ride.storages.storage_implementation \
    import StorageImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    query_params=kwargs["request_query_params"]
    print("query_params_status*******************",query_params.status)
    limit = query_params.limit
    offset = query_params.offset
    status = query_params.status
    sort_by = query_params.sort_by
    order_by = query_params.order_by
    user_id = user.id

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetMyRideRequestsInteractor(storage=storage,
                                             presenter=presenter)

    request_dict=interactor.get_my_ride_requests(
        offset =offset,
        limit=limit,
        user_id = user_id,
        order_by=order_by,
        sort_by=sort_by,
        status = status
        )
    print(request_dict)
    response_data = json.dumps(request_dict)
    return HttpResponse(response_data, status=200)