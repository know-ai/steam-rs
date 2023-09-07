from app.extensions.db import db
from datetime import datetime
from .reviews import Reviews
from .funny_reviews import FunnyReviews
from .helpful_reviews import HelpfulReviews
from .games import Games
from .playtime import Playtime


DATE_FORMAT = "%Y-%m-%d"

class Users(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.String(50), primary_key=True, unique=True)
    steam_id = db.Column(db.String(50), unique=True)
    reviews = db.relationship('Reviews', backref='user', lazy='dynamic', cascade="all, delete")
    funny_reviews = db.relationship('FunnyReviews', backref='user', lazy='dynamic', cascade="all, delete")
    helpful_reviews = db.relationship('HelpfulReviews', backref='user', lazy='dynamic', cascade="all, delete")
    playtime = db.relationship('Playtime',  backref='user', lazy='dynamic', cascade="all, delete")

    def __repr__(self):

        return f'<{self.__tablename__} {self.id}>'
    
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
        
    def vote_for_helpful_review(self, review:Reviews, helpful:bool):
        """Documentation here
        """
        if review.user_id != self.id:

            if review not in self.helpful_reviews:

                HelpfulReviews.add(user_id=self.id, helpful=helpful, review_id=review.id)

        else:

            return None
        
    def buy_game(self, game:Games):
        """Documentation here
        """
        if game not in self.games:

            self.games.append(game)
        
    def set_playtime(self, game:Games, playtime_forever:float, playtime_2weeks:float):
        """Documentation here
        """
        play_time = Playtime.add(
            game_id=game.id,
            user_id=self.id,
            playtime_forever=playtime_forever,
            playtime_2weeks=playtime_2weeks
        )
        db.session.add(play_time)
        db.session.commit()

    def serialize(self):
        """Documentation here
        """
        games = list()
        
        for game in self.games:
            
            playtime = Playtime.filter_by_user_and_game(user_id=self.id, game_id=game.id)
            if playtime is None:
                playtime = {"playtime_forever": 0, "playtime_2weeks": 0}
            else:
                playtime = playtime.serialize()
            
            result = game.serialize()
            result.update(playtime)
            games.append(result)
        
        return {
            "id": self.id,
            "steam_id": self.steam_id,
            "games": games,
            "reviews": [review.serialize() for review in self.reviews]
        }

