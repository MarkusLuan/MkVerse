from flask import Blueprint
from flask import request, abort
import flask_restful as Rest
import flask_jwt_extended as jwt
from sqlalchemy import and_, or_, desc

import uuid
import datetime

import models
import utils
import app_singleton

class Feed (Rest.Resource):
    def get(self):
        "Endpoint para carregar o feed do usuário logado"

        uuid_logged_user = jwt.get_jwt_identity()
        
        # TODO: Fazer uma unica query
        # Obtem o usuario
        user = models.User.query.filter_by(
            uuid = uuid_logged_user
        ).first()
        if not user:
            return abort(401)

        feed = models.Feed.query.outerjoin(
            models.Followers,
            models.Followers.seguindo_id == models.Feed.user_id
        ).filter(and_(
            models.Feed.dt_remocao == None,
            or_(
                models.Feed.user_id == user.id,
                models.Followers.seguidor_id == user.id,
            )
        )).order_by(
            desc(models.Feed.dt_criacao)
        ).all()

        return [postagem.to_json() for postagem in feed]
    
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
    
    def delete(self, uuid_feed: uuid.UUID):
        "Endpoint para deletar postagem de forma virtual"

        logged_user = jwt.get_jwt_identity()
        feed = models.Feed.query.join(
            models.User, models.User.id == models.Feed.user_id
        ).filter(and_(
            models.Feed.uuid == uuid_feed,
            models.Feed.dt_remocao == None,
            models.User.uuid == logged_user
        )).first_or_404()

        feed.dt_remocao = datetime.datetime.now()
        app_singleton.db.session.merge(feed)
        app_singleton.db.session.commit()

        return feed.to_json()

# Registra endpoint
Resources = Blueprint("feed", __name__, url_prefix="/feed")
api = Rest.Api(Resources)
api.add_resource(Feed, "/", "/<uuid:uuid_feed>")