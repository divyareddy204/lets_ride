# pylint: disable=wrong-import-position

APP_NAME = "lets_ride"
OPERATION_NAME = "get_matching_ride_requests"
REQUEST_METHOD = "get"
URL_SUFFIX = "matching_requests/ride/v1/"

from .test_case_01 import TestCase01GetMatchingRideRequestsAPITestCase

__all__ = [
    "TestCase01GetMatchingRideRequestsAPITestCase"
]
