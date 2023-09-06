from .base import BaseModel
from app.extensions.db import db

class Publishers(BaseModel):

    __tablename__ = 'publishers'
    games = db.relationship('Games', backref='publisher', lazy='dynamic', cascade="all, delete") 