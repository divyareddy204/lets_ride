# pylint: disable=wrong-import-position

APP_NAME = "lets_ride"
OPERATION_NAME = "create_user"
REQUEST_METHOD = "post"
URL_SUFFIX = "signup/v1/"

from .test_case_01 import TestCase01CreateUserAPITestCase

__all__ = [
    "TestCase01CreateUserAPITestCase"
]
