from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_basicauth import BasicAuth

db = SQLAlchemy()
jwt = JWTManager()
basic_auth = BasicAuth()