from sqlalchemy import BigInteger, Uuid, ForeignKey

from .abstract_model import AbstractModel
from app_singleton import db

class Followers (AbstractModel):
    seguidor_id = db.Column(BigInteger, ForeignKey("user.id"), nullable=False)
    seguindo_id = db.Column(BigInteger, ForeignKey("user.id"), nullable=False)
    
    seguidor = db.relationship("User", back_populates="Followers")
    seguindo = db.relationship("User", back_populates="Followers")

    db.UniqueConstraint('seguidor_id', 'seguindo_id')