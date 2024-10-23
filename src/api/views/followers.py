import uuid

from rest_framework.views import APIView
from rest_framework.response import Response

class Followers (APIView):
    def get(self, request):
        "Endpoint para listar seguidores do usuário logado"

        return Response ({
            "testando": "ok1234",
            "metodo": "get"
        })
    
    def post(self, request, uuid: uuid.UUID):
        "Endpoint para seguir um usuário"

        return Response ({
            "testando": "ok1234",
            "metodo": "post"
        })
    
    def delete(self, request, uuid: uuid.UUID):
        "Endpoint para deixar de seguir um usuário"

        return Response ({
            "testando": "ok1234",
            "metodo": "delete"
        })