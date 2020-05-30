# pylint: disable=wrong-import-position

APP_NAME = "lets_ride"
OPERATION_NAME = "get_matching_asset_requests"
REQUEST_METHOD = "get"
URL_SUFFIX = "matching_requests/asset/v1/"

from .test_case_01 import TestCase01GetMatchingAssetRequestsAPITestCase

__all__ = [
    "TestCase01GetMatchingAssetRequestsAPITestCase"
]
