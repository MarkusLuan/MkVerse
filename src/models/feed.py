from sqlalchemy import BigInteger, DateTime, ForeignKey

import os

from .abstract_model import AbstractModel
from app_singleton import db

class Feed (AbstractModel):
    fields = ["texto", "likes", "has_image"]

    dt_remocao = db.Column(DateTime, nullable=True)
    texto = db.Column(db.String, nullable=False)
    likes = db.Column(db.Integer, default=0, nullable=False)
    user_id = db.Column(BigInteger, ForeignKey("user.id"), nullable=False)
    
    user = db.relationship("User")
    
    @property
    def image_path(self):
        return f"img/{self.uuid}.png"
    
    @property
    def has_image(self):
        return os.path.isfile(self.image_path)

    def to_json(self):
        j = super().to_json()

        j["created_by"] = self.user.nick
        return j