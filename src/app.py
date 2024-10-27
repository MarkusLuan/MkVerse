from flask import Flask
from flask_jwt_extended import JWTManager

from models import *
from resources import Resources
from error_handler import ErrorHandler

app = Flask(__name__)
app.register_blueprint(Resources)

import app_singleton

app.config.from_object("config.development")
if "DATABASE" in app.config:
    db_config = app.config["DATABASE"]
    db_uri = "{ENGINE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}".format(
        **db_config
    )
    
    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False

app_singleton.jwt.init_app(app)
app_singleton.basic_auth.init_app(app)
app_singleton.db.init_app(app)
ErrorHandler(app)

with app.app_context():
    app_singleton.db.drop_all()
    app_singleton.db.create_all()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=80,
        debug=True
    )