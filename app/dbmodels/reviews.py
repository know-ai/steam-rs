from app.extensions.db import db
from datetime import datetime


DATE_FORMAT = "%Y-%m-%d"

class Reviews(db.Model):

    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    recommend = db.Column(db.Boolean, nullable=True)
    review = db.Column(db.String, nullable=True)
    posted = db.Column(db.DateTime())
    last_edited = db.Column(db.DateTime(), nullable=True)
    funny = db.relationship('FunnyReviews', backref='review', lazy='dynamic', cascade="all, delete") 
    helpful = db.relationship('HelpfulReviews', backref='review', lazy='dynamic', cascade="all, delete")
    user_id = db.Column(db.String(50), db.ForeignKey('users.id')) 

    def __repr__(self):

        return f'<{self.__tablename__} {self.id} - {self.review}>'
    
    @classmethod
    def add(
        cls, 
        user_id:str,
        review:str,
        recommend:bool,
        posted:str=datetime.now().date().strftime(DATE_FORMAT),
        ):
        """Documentation here
        """
        attr = cls(
            user_id=user_id,
            recommend=recommend,
            posted=datetime.strptime(posted, DATE_FORMAT),
            review=review
        )
        db.session.add(attr)
        db.session.commit()

        return attr
    
    def serialize(self):
        """
        Documentation here
        """

        return {
            "user_id": self.user_id,
            "recommend": self.recommend,
            "review": self.review,
            "posted": self.posted.date().strftime(DATE_FORMAT)
        }
        