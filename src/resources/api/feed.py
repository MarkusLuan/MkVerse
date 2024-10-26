from flask import Blueprint
from flask import request, abort
import flask_restful as Rest
import flask_jwt_extended as jwt

import uuid

import models
import utils
import app_singleton

class Feed (Rest.Resource):
    def get(self):
        "Endpoint para carregar o feed do usuário logado"

        return {
            "testando": "ok1234",
            "metodo": "get"
        }
    
    def post(self):
        "Endpoint para criar uma postagem"

        if not request.is_json:
            return abort(400)
        
        j: dict = request.get_json()
        utils.checar_campos_obrigatorios(j, ["texto"])
        utils.remover_campos(j, ["id", "uuid", "dt_criacao"])

        logged_user = jwt.get_jwt_identity()
        user = models.User.query.filter_by(
            uuid=logged_user
        ).first()

        if not user:
            return abort(401)

        # Ajustando informações - que não vem no POST
        j["dt_remocao"] = None
        j["likes"] = 0
        j["user_id"] = user.id
        
        feed = models.Feed(**j)
        app_singleton.db.session.add(feed)
        app_singleton.db.session.commit()

        # TODO: Enviar imagem

        return feed.to_json()
    
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