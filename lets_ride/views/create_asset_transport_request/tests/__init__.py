# pylint: disable=wrong-import-position

APP_NAME = "lets_ride"
OPERATION_NAME = "create_asset_transport_request"
REQUEST_METHOD = "post"
URL_SUFFIX = "asset_transport_request/v1/"

from .test_case_01 import TestCase01CreateAssetTransportRequestAPITestCase

__all__ = [
    "TestCase01CreateAssetTransportRequestAPITestCase"
]
