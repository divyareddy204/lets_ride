# pylint: disable=wrong-import-position

APP_NAME = "lets_ride"
OPERATION_NAME = "create_share_ride"
REQUEST_METHOD = "post"
URL_SUFFIX = "ride_share/v1/"

from .test_case_01 import TestCase01CreateShareRideAPITestCase

__all__ = [
    "TestCase01CreateShareRideAPITestCase"
]
