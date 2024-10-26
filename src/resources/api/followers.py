from flask import Blueprint
from flask import abort
import flask_restful as Rest
import flask_jwt_extended as jwt
from werkzeug.exceptions import BadRequest
from sqlalchemy import and_
from sqlalchemy.orm import aliased

import uuid
import datetime

import models
import app_singleton

class Followers (Rest.Resource):
    def get(self):
        "Endpoint para listar seguidores do usuário logado"

        logged_user = jwt.get_jwt_identity()
        followers = models.Followers.query.join(
            models.User,
            models.Followers.seguindo_id == models.User.id
        ).filter(
            models.User.uuid == str(logged_user)
        ).all()

        res = {
            "dt_consulta": datetime.datetime.now().isoformat(),
            "seguidores": [follower.seguidor.nick for follower in followers]
        }

        return res
    
    def post(self, uuid_user: uuid.UUID):
        "Endpoint para seguir um usuário"

        # Evitar que o usuário siga ele mesmo
        uuid_logged_user = jwt.get_jwt_identity()
        if str(uuid_logged_user) == str(uuid_user):
            raise BadRequest("Não é possivel seguir você mesmo!")

        # Checa e Obtem Usuario Logado
        logged_user = models.User.query.filter_by(
            uuid = str(uuid_logged_user)
        ).first()
        if not logged_user:
            return abort(401)
        
        # Checa e Obtem Usuario Informado
        user = models.User.query.filter_by(
            uuid = str(uuid_user)
        ).first_or_404("Usuario não encontrado!")

        # Checa se já segue
        follower = models.Followers.query.filter(
            and_(
                models.Followers.seguidor_id == logged_user.id,
                models.Followers.seguindo_id == user.id
            )
        ).first()
        if follower:
            raise Exception(f"Você já segue {user.nick}!")

        follower = models.Followers(
            seguidor_id = logged_user.id,
            seguindo_id = user.id
        )

        app_singleton.db.session.add(follower)
        app_singleton.db.session.commit()

        return follower.to_json()
    
    def delete(self, uuid_user: uuid.UUID):
        "Endpoint para deixar de seguir um usuário - Deleta fisicamente do DB"

        # Evitar que o usuário siga ele mesmo
        uuid_logged_user = jwt.get_jwt_identity()
        if str(uuid_logged_user) == str(uuid_user):
            raise BadRequest("Não é possivel deixar de seguir você mesmo!")
        
        user_seguindo = aliased(models.User)
        user_seguidor = aliased(models.User)
        
        follower = models.Followers.query.join(
            user_seguindo, models.Followers.seguindo
        ).join(
            user_seguidor, models.Followers.seguidor
        ).filter(
            user_seguindo.uuid == str(uuid_user),
            user_seguidor.uuid == str(uuid_logged_user),
        ).first_or_404("Você não segue este usuário!")

        # Hack para carregar os atributos Lazy Load
        _, _ = follower.seguidor, follower.seguindo

        # Remoção Fisica
        # Como não tem outra relação não seria um problema
        # e também poupa espaço no banco
        app_singleton.db.session.delete(follower)
        app_singleton.db.session.commit()

        return follower.to_json()
        
# Registra endpoint
Resources = Blueprint("followers", __name__, url_prefix="/followers")
api = Rest.Api(Resources)
api.add_resource(Followers, "/", "/<uuid:uuid_user>")