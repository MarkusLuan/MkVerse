from flask import Blueprint
from flask import request, abort, send_file
import flask_restful as Rest
import flask_jwt_extended as jwt
from werkzeug.exceptions import BadRequest
from sqlalchemy import and_, or_, desc

import os
import uuid
import datetime
import re

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
            uuid = str(uuid_logged_user)
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
        
        j = {}
        if request.is_json:
            j: dict = request.get_json()
        else:
            j = request.form.to_dict()
        
        utils.checar_campos_obrigatorios(j, ["texto"])
        utils.remover_campos(j, ["id", "uuid", "dt_criacao"])

        logged_user = jwt.get_jwt_identity()
        user = models.User.query.filter_by(
            uuid = str(logged_user)
        ).first()

        if not user:
            return abort(401)
        
        # Verifica se possui imagem
        img = request.files.get("imagem", None)
        if img:
            pattern = re.compile("image/*")
            print(img.mimetype)
            if not pattern.match(img.mimetype):
                raise BadRequest("O arquivo enviado não é uma imagem!")
            
            if not os.path.isdir("img/"):
                os.mkdir("img/")

        # Ajustando informações - que não vem no POST
        j["dt_remocao"] = None
        j["likes"] = 0
        j["user_id"] = user.id
        
        feed = models.Feed(**j)
        app_singleton.db.session.add(feed)
        app_singleton.db.session.commit()
        
        # Salvar imagem se houver
        if img:
            img.save(feed.image_path)

        return feed.to_json()
    
    def delete(self, uuid_feed: uuid.UUID):
        "Endpoint para deletar postagem de forma virtual"

        logged_user = jwt.get_jwt_identity()
        feed = models.Feed.query.join(
            models.User, models.User.id == models.Feed.user_id
        ).filter(and_(
            models.Feed.uuid == str(uuid_feed),
            models.Feed.dt_remocao == None,
            models.User.uuid == str(logged_user)
        )).first_or_404()

        feed.dt_remocao = datetime.datetime.now()
        app_singleton.db.session.merge(feed)
        app_singleton.db.session.commit()

        return feed.to_json()

# Registra endpoint
Resources = Blueprint("feed", __name__, url_prefix="/feed")
api = Rest.Api(Resources)
api.add_resource(Feed, "", "/", "/<uuid:uuid_feed>")

@Resources.route("/<uuid:uuid_feed>/img")
def get_feed_img(uuid_feed: uuid.UUID):
    
    uuid_logged_user = jwt.get_jwt_identity()
    # Obtem o usuario
    user = models.User.query.filter_by(
        uuid = str(uuid_logged_user)
    ).first()
    if not user:
        return abort(401)
    
    feed = models.Feed.query.outerjoin(
        models.Followers,
        models.Followers.seguindo_id == models.Feed.user_id
    ).filter(and_(
        models.Feed.uuid == str(uuid_feed),
        models.Feed.dt_remocao == None,
        or_(
            models.Feed.user_id == user.id,
            models.Followers.seguidor_id == user.id,
        )
    )).first_or_404()
    
    if not feed.has_image:
        return abort(404)
    
    return send_file(feed.image_path, mimetype="image/*", as_attachment=False)