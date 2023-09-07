from app.extensions.db import db


class Playtime(db.Model):

    __tablename__ = 'playtime'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    playtime_forever = db.Column(db.Float)
    playtime_2weeks = db.Column(db.Float)

    def __repr__(self):

        return f'<{self.__tablename__} {self.id} - game {self.game_id} - user {self.user_id}>'
    
    @classmethod
    def add(cls, user_id:str, game_id:str, playtime_forever:float=0, playtime_2weeks:float=0):
        """Documentation here
        """
        if not cls.user_id_exists(user_id):

            attr = cls(
                user_id=user_id,
                game_id=game_id,
                playtime_forever=playtime_forever,
                playtime_2weeks=playtime_2weeks
            )
            db.session.add(attr)
            db.session.commit()

            return attr
        
        else:

            if not cls.game_id_exists(game_id):

                attr = cls(
                    user_id=user_id,
                    game_id=game_id,
                    playtime_forever=playtime_forever,
                    playtime_2weeks=playtime_2weeks
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
        
    @classmethod
    def user_id_exists(cls, user_id:int):
        r"""
        Documentation here
        """
        attr = cls.get(user_id=user_id)

        if attr:
            
            return True
        
        return False
    
    @classmethod
    def game_id_exists(cls, game_id:int):
        r"""
        Documentation here
        """
        attr = cls.get(game_id=game_id)

        if attr:
            
            return True
        
        return False
    
    @classmethod
    def filter_by_user_and_game(cls, user_id:str, game_id:int):
        """Documentation here
        """
        return cls.get(user_id=user_id, game_id=game_id)
    
    def serialize(self)->dict:
        """Documenation here
        """
        return {
            "playtime_forever": self.playtime_forever,
            "playtime_2weeks": self.playtime_2weeks
        }