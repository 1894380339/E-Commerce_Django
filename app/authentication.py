import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication


class SafeJWTAuthentication(BaseAuthentication):
    pass

    def authenticate(self, request):

        User = get_user_model()
        authorization_heaader = request.headers.get("Authorization")

        if not authorization_heaader:
            return None
        try:
            # header = 'Token xxxxxxxxxxxxxxxxxxxxxxxx'
            access_token = authorization_heaader.split(" ")[1]
            payload = jwt.decode(
                access_token,
                settings.SECRET_KEY,
                algorithms=["HS256"],
            )

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("access_token expired")
        except IndexError:
            raise exceptions.AuthenticationFailed("Token prefix missing")

        user = User.objects.filter(id=payload["user_id"]).first()
        if user is None:
            raise exceptions.AuthenticationFailed("User not found")

        if not user.is_active:
            raise exceptions.AuthenticationFailed("user is inactive")

        self.enforce_csrf(request)
        return (user, None)
