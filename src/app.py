from flask import Flask

from resources import Resources
from error_handler import ErrorHandler
import app_singleton

def create_app(config_object):
    app = Flask(__name__)
    app.register_blueprint(Resources)

    app.config.from_object(config_object)
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
    app_singleton.migrate.init_app(app, app_singleton.db)
    ErrorHandler(app)
    
    return app

if __name__ == "__main__":
    app = create_app("config.development")
    app.run(
        host="0.0.0.0",
        port=80,
        debug=True
    )