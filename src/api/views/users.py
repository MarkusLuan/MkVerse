import uuid

from rest_framework.views import APIView
from rest_framework.response import Response

class Users (APIView):
    def get(self, request):
        "Endpoint para procurar usuários"

        return Response ({
            "testando": "ok1234",
            "metodo": "get"
        })
    
    def post(self, request):
        "Endpoint para criar Usuario"

        return Response ({
            "testando": "ok1234",
            "metodo": "post"
        })

class UserInfo (APIView):
    def get(self, request, uuid: uuid.UUID):
        "Endpoint para verificar informações do usuário (Nome, Quantidade de Seguidores e Quantos seguem ele)"

        return Response({
            "testando": "ok213",
            "metodo": "get",
            "uuid": uuid
        })