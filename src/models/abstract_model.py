from sqlalchemy import Uuid, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app_singleton import db

class AbstractModel (db.Model):
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(Uuid, unique=True, nullable=False)
    dt_criacao = db.Column(DateTime, unique=True, nullable=False)