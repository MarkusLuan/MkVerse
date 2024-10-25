from flask import Blueprint
import flask_restful as Rest

import uuid
import app_singleton

class Users (Rest.Resource):
    def get(self):
        "Endpoint para procurar usuários - Unico metodo com Basic Auth"

        return {
            "testando": "ok1234",
            "metodo": "get"
        }
    
    @app_singleton.basic_auth.required
    def post(self):
        "Endpoint para criar Usuario"

        return {
            "testando": "ok1234",
            "metodo": "post"
        }

class UserInfo (Rest.Resource):
    def get(self, uuid: uuid.UUID):
        "Endpoint para verificar informações do usuário (Nome, Quantidade de Seguidores e Quantos seguem ele)"

        return {
            "testando": "ok213",
            "metodo": "get",
            "uuid": str(uuid)
        }

# Registra endpoint
Resources = Blueprint("users", __name__, url_prefix="/users")
api = Rest.Api(Resources)
api.add_resource(Users, "/")
api.add_resource(UserInfo, "/<uuid:uuid>")