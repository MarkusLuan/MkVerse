from flask import Blueprint
from flask import request, abort, jsonify
import flask_restful as Rest
from werkzeug.exceptions import BadRequest
from sqlalchemy import and_, or_

import uuid

import models
import utils
import app_singleton

class Users (Rest.Resource):
    def get(self):
        "Endpoint para procurar usuários"
        search = request.args.get("user", type=str, default="")
        if not search:
            raise BadRequest("É necessário informar a busca usando o parametro 'user'!")

        users = models.User.query.filter(or_(
            models.User.nick.like(f'%{search}%'),
            models.User.nome.like(f"%{search}%")
        )).all()

        return jsonify([user.to_json() for user in users])
    
    @app_singleton.basic_auth.required
    def post(self):
        "Endpoint para criar Usuario - Unico metodo com Basic Auth"

        if not request.is_json:
            return abort(400)
        
        j: dict = request.get_json()
        utils.checar_campos_obrigatorios(j, [
            "dt_nascimento",
            "username",
            "nome",
            "email",
            "bio",
            "password",
        ])
        
        utils.remover_campos(j, ["id", "uuid", "dt_criacao"])
        
        # Pequena troca para confundir SQL Injection - Sei que não é o bastante, mas...
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
    def get(self, uuid_user: uuid.UUID):
        "Endpoint para verificar informações do usuário (Nome, Quantidade de Seguidores e Quantos seguem ele)"

        # TODO: Ajustar para só permitir quem o usuário segue
        user = models.User.query.filter(
            models.User.uuid == str(uuid_user)
        ).first()

        if user is None:
            return abort(404)

        return user.to_json()

# Registra endpoint
Resources = Blueprint("users", __name__, url_prefix="/users")
api = Rest.Api(Resources)
api.add_resource(Users, "/")
api.add_resource(UserInfo, "/<uuid:uuid_user>")