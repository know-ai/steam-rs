from app.extensions.db import db


class HelpfulReviews(db.Model):

    __tablename__ = 'helpful_reviews'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    helpful = db.Column(db.Boolean, nullable=True)
    user_id = db.Column(db.String(50), db.ForeignKey('users.id'))
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'))

    def __repr__(self):

        return f'<{self.__tablename__} {self.id} - is_helpful: {self.helpful} - {self.review.review}>'
    
    @classmethod
    def add(cls, user_id:str, helpful:bool, review_id:int):
        """
        Documentation here
        """
        attr = cls(
                user_id=user_id,
                helpful=helpful,
                review_id=review_id
            )
        db.session.add(attr)
        db.session.commit()

        return attr
    
    def serialize(self):
        """
        Documentation here
        """
        return {
            "id": self.id,
            "helpful": self.helpful,
            "user_id": self.user_id,
            "review": self.review.serialize()
        }