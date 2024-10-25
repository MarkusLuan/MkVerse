from flask import Blueprint

from . import users
from . import followers
from . import feed
from . import likes

Resources = Blueprint("api", __name__, url_prefix="/api")
Resources.register_blueprint(users.Resources)
Resources.register_blueprint(followers.Resources)
Resources.register_blueprint(feed.Resources)
Resources.register_blueprint(likes.Resources)