from sqlalchemy import BigInteger, DateTime, ForeignKey

from .abstract_model import AbstractModel
from app_singleton import db

class Feed (AbstractModel):
    fields = ["texto", "likes"]

    dt_remocao = db.Column(DateTime, nullable=True)
    texto = db.Column(db.String, nullable=False)
    uuid_imagem = db.Column(db.String(36), unique=True, nullable=True)
    likes = db.Column(db.Integer, default=0, nullable=False)
    user_id = db.Column(BigInteger, ForeignKey("user.id"), nullable=False)
    
    user = db.relationship("User")

    def to_json(self):
        j = super().to_json()

        j["created_by"] = self.user.nick
        j["uuid_imagem"] = str(self.uuid_imagem) if self.uuid_imagem else None
        return j