from sqlalchemy import Uuid, DateTime, sql

from app_singleton import db

import uuid

class AbstractModel (db.Model):
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(Uuid, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    dt_criacao = db.Column(DateTime, default=sql.func.now(), nullable=False)