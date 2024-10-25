import datetime
from flask import Blueprint
from flask import request, jsonify, abort
import flask_jwt_extended as jwt

import uuid

Resources = Blueprint("auth", __name__, url_prefix="/auth")

def gerar_token(identity):
    dt_agora = datetime.datetime.now()
    delta_expiracao = datetime.timedelta(hours=1)
    dt_expiracao = delta_expiracao + dt_agora
    
    res = {
        "created_at": dt_agora.timestamp(),
        "access_token": jwt.create_access_token(identity, expires_delta=delta_expiracao),
        "refresh_token": jwt.create_refresh_token(identity, delta_expiracao),
        "expires_in": dt_expiracao.timestamp()
    }
    
    return res

@Resources.route("/token", methods=["POST"])
def get_token():
    j = request.json
    if not request.is_json or not j:
        return abort(400)
    
    username = j.get("username", None)
    password = j.get("password", None)
    if username != "test" or password != "test":
        return abort(401)

    return jsonify(gerar_token(username))

@Resources.route("/refresh", methods=["POST"])
@jwt.jwt_required(refresh=True)
def refresh_token():
    identity = jwt.get_jwt_identity()
    return jsonify(gerar_token(identity))