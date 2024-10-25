from flask import Blueprint

from . import api

Resources = Blueprint("resources", __name__)
Resources.register_blueprint(api.Resources)