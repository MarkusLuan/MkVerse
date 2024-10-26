from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, relationship

from .abstract_model import AbstractModel
from app_singleton import db

class User(AbstractModel):
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
        """Serializer temporário
           * Não encontrei a implementação do Serializer do SQLAlchemy e nem FlaskREST
           * e o do Marshmellow (acho que é assim que se escreve) é horrivel de se fazer.
           * Aí como está acabando o tempo, vou usar desta forma que embora não seja abstrata, é bem prática de se fazer.
           """

        fields = ["uuid", "nick", "nome", "email", "bio"]
        j = {field: self.__getattribute__(field) for field in fields}

        j["seguidores"] = len(self.seguidores)
        j["seguindo"] = len(self.seguindo)

        return j