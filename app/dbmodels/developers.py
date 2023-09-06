from .base import BaseModel
from app.extensions.db import db


class Developers(BaseModel):

    __tablename__ = 'developers'
    games = db.relationship('Games', backref='developer', lazy='dynamic', cascade="all, delete") 