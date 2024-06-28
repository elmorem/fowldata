from django.contrib.auth.backends import BaseBackend

from .models import MyUser

class AuthenticationBackend(BaseBackend):
    """
    Authentication backend to manage the custom user model.
    """
    def authenticate(self, request, username=None, password=None):
        user = MyUser.objects.get(username=username)
        if user is not None and user.check_password(password):
            return user
        else:
            raise ValueError("User not found")
        return None