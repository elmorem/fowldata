import pytest

from accounts.models import MyUser

@pytest.fixture
def basic_user() -> MyUser:
    """Creates a basic user"""
    user = MyUser.objects.create(email="elmorem@gmail.com", name="Mark", username="elmorem")
    user.save()
    return user