import uuid

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication

from api.authentication import BasicAuthentication

class Users (APIView):
    authentication_classes = [SessionAuthentication]

    def get(self, request):
        "Endpoint para procurar usuários"

        return Response ({
            "testando": "ok1234",
            "metodo": "get"
        })
    
    def post(self, request):
        "Endpoint para criar Usuario"

        self.authentication_classes = [BasicAuthentication]
        print("tasdsnasjn")
        self.check_permissions(request)

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