from django.contrib.auth.backends import BaseBackend


class EmailAuthBackend(BaseBackend):
    """
    Custom authentication backend that allows users to log in using their email address.
    """

    def authenticate(self, request, email=None, password=None, **kwargs):
        from django.contrib.auth import get_user_model

        User = get_user_model()
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        from django.contrib.auth import get_user_model

        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None