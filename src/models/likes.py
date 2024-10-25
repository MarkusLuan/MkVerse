from sqlalchemy import BigInteger, ForeignKey

from .abstract_model import AbstractModel
from app_singleton import db

class Likes (AbstractModel):
    user_id = db.Column(BigInteger, ForeignKey("user.id"), nullable=False)
    feed_id = db.Column(BigInteger, ForeignKey("feed.id"), nullable=False)
    
    user = db.relationship("User")
    feed = db.relationship("Feed")

