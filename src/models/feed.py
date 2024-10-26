from sqlalchemy import BigInteger, Uuid, DateTime, ForeignKey

from .abstract_model import AbstractModel
from app_singleton import db

class Feed (AbstractModel):
    dt_remocao = db.Column(db.String, nullable=True)
    texto = db.Column(DateTime, nullable=False)
    uuid_imagem = db.Column(Uuid, unique=True, nullable=True)
    likes = db.Column(BigInteger, default=0, nullable=False)
    user_id = db.Column(BigInteger, ForeignKey("user.id"), nullable=False)
    
    user = db.relationship("User")
