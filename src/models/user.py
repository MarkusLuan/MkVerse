from sqlalchemy import DateTime

from .abstract_model import AbstractModel
from app_singleton import db

class User(AbstractModel):
    dt_nascimento = db.Column(DateTime, unique=True, nullable=False)
    nick = db.Column(db.String, nullable=False)
    nome = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    bio = db.Column(db.String, nullable=False)
    senha = db.Column(db.String, nullable=False)    

    def __str__(self):
        return self.nick