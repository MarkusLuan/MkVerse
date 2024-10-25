from flask import Blueprint
import flask_restful as Rest

import uuid

class Followers (Rest.Resource):
    def get(self):
        "Endpoint para listar seguidores do usuário logado"

        return {
            "testando": "ok1234",
            "metodo": "get"
        }
    
    def post(self, uuid: uuid.UUID):
        "Endpoint para seguir um usuário"

        return {
            "testando": "ok1234",
            "metodo": "post"
        }
    
    def delete(self, uuid: uuid.UUID):
        "Endpoint para deixar de seguir um usuário"

        return {
            "testando": "ok1234",
            "metodo": "delete"
        }
        
# Registra endpoint
Resources = Blueprint("followers", __name__, url_prefix="/followers")
api = Rest.Api(Resources)
api.add_resource(Followers, "/", "/<uuid:uuid>")