# pylint: disable=wrong-import-position

APP_NAME = "lets_ride"
OPERATION_NAME = "get_my_asset_transport_requests"
REQUEST_METHOD = "get"
URL_SUFFIX = "my_requests/asset/v1/"

from .test_case_01 import TestCase01GetMyAssetTransportRequestsAPITestCase

__all__ = [
    "TestCase01GetMyAssetTransportRequestsAPITestCase"
]
