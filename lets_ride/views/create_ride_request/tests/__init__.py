# pylint: disable=wrong-import-position

APP_NAME = "lets_ride"
OPERATION_NAME = "create_ride_request"
REQUEST_METHOD = "post"
URL_SUFFIX = "ride_request/v1/"

from .test_case_01 import TestCase01CreateRideRequestAPITestCase

__all__ = [
    "TestCase01CreateRideRequestAPITestCase"
]
