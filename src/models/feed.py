from sqlalchemy import BigInteger, Uuid, DateTime, ForeignKey

from .abstract_model import AbstractModel
from app_singleton import db

class Feed (AbstractModel):
    fields = ["texto", "likes"]

    dt_remocao = db.Column(DateTime, nullable=True)
    texto = db.Column(db.String, nullable=False)
    uuid_imagem = db.Column(Uuid, unique=True, nullable=True)
    likes = db.Column(BigInteger, default=0, nullable=False)
    user_id = db.Column(BigInteger, ForeignKey("user.id"), nullable=False)
    
    user = db.relationship("User")

    def __to_json(self):
        j = super().to_json()

        j["uuid_imagem"] = str(self.uuid_imagem) if self.uuid_imagem else None
        return j