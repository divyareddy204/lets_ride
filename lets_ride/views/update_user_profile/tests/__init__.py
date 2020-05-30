# pylint: disable=wrong-import-position

APP_NAME = "lets_ride"
OPERATION_NAME = "update_user_profile"
REQUEST_METHOD = "post"
URL_SUFFIX = "useprofile/v1/"

from .test_case_01 import TestCase01UpdateUserProfileAPITestCase

__all__ = [
    "TestCase01UpdateUserProfileAPITestCase"
]
