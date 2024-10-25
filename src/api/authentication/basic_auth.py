from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings

class BasicAuthentication (BaseAuthentication):
    def authenticate(self, request):
        print("teste")

        auth = request.headers.get('Authorization')
        if not auth or not auth.startswith('Basic ') or auth.replace('Basic ', '') != settings.BASIC_API_KEY:
            raise AuthenticationFailed('Acesso não permitido: Autenticação invalida!')

        return ("api_user", None)