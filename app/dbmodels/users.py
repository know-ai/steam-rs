from app.extensions.db import db
from datetime import datetime
from .reviews import Reviews
from .funny_reviews import FunnyReviews


DATE_FORMAT = "%Y-%m-%d"

class Users(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.String(50), primary_key=True, unique=True)
    steam_id = db.Column(db.String(50), unique=True)
    reviews = db.relationship('Reviews', backref='user', lazy='dynamic', cascade="all, delete")
    funny_reviews = db.relationship('FunnyReviews', backref='user', lazy='dynamic', cascade="all, delete")
    helpful_reviews = db.relationship('HelpfulReviews', backref='user', lazy='dynamic', cascade="all, delete")

    def __repr__(self):

        return f'<{self.__tablename__} {self.id} - {self.name}>'
    
    @classmethod
    def add(cls, id:str, steam_id:str):
        """Documentation here
        """
        if (not cls.id_exists(id) and not cls.steam_id_exists(steam_id)):

            attr = cls(
                id=id,
                steam_id=steam_id
            )
            db.session.add(attr)
            db.session.commit()

            return attr
        
    @classmethod
    def get(cls, first=True, **fields):
        
        obj = cls.query.filter_by(**fields)

        if obj:

            if first:

                obj = obj.first()

            return obj
        
        else:

            raise ValueError(f"record {fields} not exists into {cls.__tablename__}, please add it")
        
    def add_review(self, review:str, recommend:bool, posted:str=datetime.now().date().strftime(DATE_FORMAT)):
        """
        Documentation here
        """

        return Reviews.add(
            review=review,
            recommend=recommend,
            posted=posted
        )
        
    @classmethod
    def id_exists(cls, id:int):
        r"""
        Documentation here
        """
        attr = cls.get(id=id)

        if attr:
            
            return True
        
        return False
    
    @classmethod
    def steam_id_exists(cls, id:int):
        r"""
        Documentation here
        """
        attr = cls.get(steam_id=id)

        if attr:
            
            return True
        
        return False
    
    def vote_for_funny_review(self, review:Reviews, funny:bool):
        """Documentation here
        """
        if review.user_id != self.id:

            if review not in self.funny_reviews:

                FunnyReviews.add(user_id=self.id, funny=funny, review_id=review.id)

        else:

            return None