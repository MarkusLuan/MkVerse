import uuid

from rest_framework.views import APIView
from rest_framework.response import Response

class Feed (APIView):
    def get(self, request):
        "Endpoint para carregar o feed do usuário logado"

        return Response ({
            "testando": "ok1234",
            "metodo": "get"
        })
    
    def post(self, request):
        "Endpoint para criar uma postagem"

        return Response ({
            "testando": "ok1234",
            "metodo": "post"
        })
    
    def delete(self, request, uuid: uuid.UUID):
        "Endpoint para deletar postagem"

        return Response ({
            "testando": "ok1234",
            "metodo": "delete"
        })