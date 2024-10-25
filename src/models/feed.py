from sqlalchemy import BigInteger, Uuid, ForeignKey

from .abstract_model import AbstractModel
from app_singleton import db

class Feed (AbstractModel):
    texto = db.Column(db.String, nullable=False)
    uuid_imagem = db.Column(Uuid, unique=True, nullable=True)
    user_id = db.Column(BigInteger, ForeignKey("user.id"), nullable=False)
    
    user = db.relationship("User", back_populates="Feed")
