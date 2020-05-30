# pylint: disable=wrong-import-position

APP_NAME = "lets_ride"
OPERATION_NAME = "get_my_ride_requests"
REQUEST_METHOD = "get"
URL_SUFFIX = "my_requests/ride/v1/"

from .test_case_01 import TestCase01GetMyRideRequestsAPITestCase

__all__ = [
    "TestCase01GetMyRideRequestsAPITestCase"
]
