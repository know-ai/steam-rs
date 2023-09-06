from app.extensions.db import db


class HelpfulReviews(db.Model):

    __tablename__ = 'helpful_reviews'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    helpful = db.Column(db.Boolean, nullable=True)
    user_id = db.Column(db.String(50), db.ForeignKey('users.id'))
    review_id = db.Column(db.Integer, db.ForeignKey('reviews.id'))

    def __repr__(self):

        return f'<{self.__tablename__} {self.id} - is_funny: {self.funny} - {self.review.review}>'