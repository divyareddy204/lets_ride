# pylint: disable=wrong-import-position

APP_NAME = "lets_ride"
OPERATION_NAME = "change_password"
REQUEST_METHOD = "post"
URL_SUFFIX = "user_profile/change_password/v1/"

from .test_case_01 import TestCase01ChangePasswordAPITestCase

__all__ = [
    "TestCase01ChangePasswordAPITestCase"
]
