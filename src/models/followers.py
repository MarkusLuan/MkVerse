from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped

from .abstract_model import AbstractModel
from app_singleton import db

class Followers (AbstractModel):
    seguidor_id = db.Column(BigInteger, ForeignKey("user.id"), nullable=False)
    seguindo_id = db.Column(BigInteger, ForeignKey("user.id"), nullable=False)
    
    seguidor = db.relationship("User", foreign_keys=[seguidor_id], back_populates="seguindo")
    seguindo = db.relationship("User", foreign_keys=[seguindo_id], back_populates="seguidores")

    __table_args__ = (
        db.UniqueConstraint('seguidor_id', 'seguindo_id'),
    )

    def to_json(self):
        j = super().to_json()

        j["seguidor"] = self.seguidor.nick
        j["seguindo"] = self.seguindo.nick

        return j