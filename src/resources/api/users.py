from flask import Blueprint
from flask import request, abort, jsonify
import flask_restful as Rest
from werkzeug.exceptions import BadRequest

import uuid
import datetime

import models
import utils
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

        if not request.is_json:
            return abort(400)
        
        j: dict = request.get_json()
        try:
            utils.checar_campos_obrigatorios(j, [
                "dt_nascimento",
                "username",
                "nome",
                "email",
                "bio",
                "password",
            ])
        except ValueError as e:
            raise BadRequest(str(e))
        
        # Removendo campos que são gerados automaticamente
        for campo in ["id", "uuid", "dt_criacao"]:
            if campo in j:
                del j[campo]
        
        # Pequena troca para confundir SQL Injection
        j["nick"] = j.pop("username")
        j["senha"] = j.pop("password")
        user = models.User(**j)

        try:
            app_singleton.db.session.add(user)
            app_singleton.db.session.commit()
        except Exception as e:
            print(e)
            raise Exception("Ocorreu algum erro ao salvar os dados no banco!")

        return {
            "uuid": str(user.uuid),
            "dt_criacao": user.dt_criacao.isoformat(),
            "username": user.nick,
            "email": user.email,
            "nome": user.nome,
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