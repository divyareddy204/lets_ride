import pytest
from lets_ride.models import User


@pytest.fixture()
def create_users():
    users = [
        {
            'username': 'ram',
            "mobile_number": "890235",
            "password": "password"
        },
        {
            'username': 'sham',
            "mobile_number": "890235",
            "password": "password"
        }
    ]

    for user in users:
        User.objects.create(
            username=user['username'],
            password=user["password"],
            mobile_number=user["mobile_number"])
