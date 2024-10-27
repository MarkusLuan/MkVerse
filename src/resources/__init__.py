from flask import Blueprint
from flask import request
import flask_jwt_extended as jwt

from . import api

Resources = Blueprint("resources", __name__)
Resources.register_blueprint(api.Resources)

@Resources.before_app_request
def verify_jwt():
    "Função para bloquear toda requisição não autenticada"
    
    rule = request.url.replace(
        request.url_root, ""
    ).strip("/")
    
    # Se a url for /api/user ou /api/auth/* autorizar acesso com BasicAuth
    is_bloquear = not (rule.endswith("api/users") and request.method == "POST") \
        and not (rule.startswith("api/auth"))
    
    if is_bloquear:
        jwt.verify_jwt_in_request()