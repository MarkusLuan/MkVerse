from flask import Blueprint
import flask_restful as Rest

import uuid

class Likes (Rest.Resource):
    def post(self, uuid: uuid.UUID):
        "Endpoint para curtir uma postagem"

        return {
            "testando": "ok1234",
            "metodo": "post"
        }
    
    def delete(self, uuid: uuid.UUID):
        "Endpoint para descurtir uma postagem"

        return {
            "testando": "ok1234",
            "metodo": "delete"
        }

# Registra endpoint
Resources = Blueprint("likes", __name__, url_prefix="/likes")
api = Rest.Api(Resources)
api.add_resource(Likes, "/<uuid:uuid>")