import uuid

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class AuthToken (TokenObtainPairView):
    pass

class AuthRefreshToken (TokenRefreshView):
    pass