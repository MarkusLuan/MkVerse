from flask import Blueprint
from flask import abort
import flask_restful as Rest
import flask_jwt_extended as jwt
from werkzeug.exceptions import BadRequest
from sqlalchemy import and_

import uuid

import models
import app_singleton

class Likes (Rest.Resource):
    def get(self, uuid_feed: uuid.UUID):
        "Endpoint para listar curtidas"
        
        likes = models.Likes.query.join(
            models.Feed, models.Feed.id == models.Likes.feed_id
        ).filter(and_(
            # models.Feed.uuid != None,## str(uuid_feed),
            models.Feed.dt_remocao == None
        )).all()
        
        return [like.to_json() for like in likes]
    
    def post(self, uuid_feed: uuid.UUID):
        "Endpoint para curtir uma postagem"

        uuid_logged_user = jwt.get_jwt_identity()
        user = models.User.query.filter_by(
            uuid = str(uuid_logged_user)
        ).first()
        if not user:
            return abort(401)
        
        feed = models.Feed.query.filter(and_(
            models.Feed.uuid == str(uuid_feed),
            models.Feed.dt_remocao == None
        )).first_or_404("Postagem não encontrada!")

        # Atualiza a contagem em cache de likes
        feed.likes += 1
        
        if str(feed.user.uuid) == str(uuid_logged_user):
            raise BadRequest("Você não pode curtir sua propria postagem!")
        
        like = models.Likes.query.filter(and_(
            models.Likes.feed_id == feed.id,
            models.Likes.user_id == user.id
        )).first()

        if like:
            raise BadRequest("Você já curtiu essa postagem!")
        
        like = models.Likes(
            user_id = user.id,
            feed_id = feed.id
        )
        
        # Finaliza as gravações
        app_singleton.db.session.add(like)
        app_singleton.db.session.merge(feed)
        app_singleton.db.session.commit()
        
        return feed.to_json()
    
    def delete(self, uuid_feed: uuid.UUID):
        "Endpoint para descurtir uma postagem"
        
        uuid_logged_user = jwt.get_jwt_identity()
        user = models.User.query.filter_by(
            uuid = str(uuid_logged_user)
        ).first()
        if not user:
            return abort(401)
        
        feed = models.Feed.query.filter(and_(
            models.Feed.uuid == str(uuid_feed),
            models.Feed.dt_remocao == None
        )).first_or_404("Postagem não encontrada!")

        # Atualiza a contagem de likes em cache
        feed.likes -= 1
        
        if str(feed.user.uuid) == str(uuid_logged_user):
            raise BadRequest("Você não pode curtir sua propria postagem!")
        
        like = models.Likes.query.filter(and_(
            models.Likes.feed_id == feed.id,
            models.Likes.user_id == user.id
        )).first()

        if not like:
            raise BadRequest("Você ainda não curtiu essa postagem!")
        
        # Realiza remoção fisica
        app_singleton.db.session.delete(like)
        
        # Finaliza as gravações
        app_singleton.db.session.merge(feed)
        app_singleton.db.session.commit()

        return feed.to_json()

# Registra endpoint
Resources = Blueprint("likes", __name__, url_prefix="/likes")
api = Rest.Api(Resources)
api.add_resource(Likes, "/<uuid:uuid_feed>")