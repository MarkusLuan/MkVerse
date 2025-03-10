from sqlalchemy import DateTime
from sqlalchemy.orm import relationship

from .abstract_model import AbstractModel
from app_singleton import db

class User(AbstractModel):
    fields = ["nick", "nome", "email", "bio"]

    dt_nascimento = db.Column(DateTime, nullable=False)
    nick = db.Column(db.String, unique=True, nullable=False)
    nome = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    bio = db.Column(db.String, nullable=False)
    senha = db.Column(db.String, nullable=False)

    seguindo = relationship("Followers", foreign_keys="[Followers.seguidor_id]", back_populates="seguidor")
    seguidores = relationship("Followers", foreign_keys="[Followers.seguindo_id]", back_populates="seguindo")

    def __str__(self):
        return self.nick
    
    def to_json(self):
        j = super().to_json()

        j["seguidores"] = len(self.seguidores)
        j["seguindo"] = len(self.seguindo)

        return j