from flask import Blueprint
import flask_restful as Rest

import uuid

class Feed (Rest.Resource):
    def get(self):
        "Endpoint para carregar o feed do usuário logado"

        return {
            "testando": "ok1234",
            "metodo": "get"
        }
    
    def post(self):
        "Endpoint para criar uma postagem"

        return {
            "testando": "ok1234",
            "metodo": "post"
        }
    
    def delete(self, uuid: uuid.UUID):
        "Endpoint para deletar postagem"

        return {
            "testando": "ok1234",
            "metodo": "delete"
        }

# Registra endpoint
Resources = Blueprint("feed", __name__, url_prefix="/feed")
api = Rest.Api(Resources)
api.add_resource(Feed, "/", "/<uuid:uuid>")