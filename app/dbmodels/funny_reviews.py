from app.extensions.db import db
from .reviews import Reviews


class FunnyReviews(db.Model):

    __tablename__ = 'funny_reviews'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    funny = db.Column(db.Boolean, nullable=True)
    user_id = db.Column(db.String(50), db.ForeignKey('users.id'))
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'))

    def __repr__(self):

        return f'<{self.__tablename__} {self.id} - is_funny: {self.funny} - {self.review.review}>'
    
    @classmethod
    def add(cls, user_id:str, funny:bool, review_id:int):
        """
        Documentation here
        """
        attr = cls(
                user_id=user_id,
                funny=funny,
                review_id=review_id
            )
        db.session.add(attr)
        db.session.commit()

        return attr