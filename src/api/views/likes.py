import uuid

from rest_framework.views import APIView
from rest_framework.response import Response

class Likes (APIView):
    def post(self, request, uuid: uuid.UUID):
        "Endpoint para curtir uma postagem"

        return Response ({
            "testando": "ok1234",
            "metodo": "post"
        })
    
    def delete(self, request, uuid: uuid.UUID):
        "Endpoint para descurtir uma postagem"

        return Response ({
            "testando": "ok1234",
            "metodo": "delete"
        })