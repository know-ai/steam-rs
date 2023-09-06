from app.extensions.db import db


class Reviews(db.Model):

    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    funny = db.Column(db.Integer, nullable=True)
    posted = db.Column(db.DateTime())
    last_edited = db.Column(db.DateTime(), nullable=True)
    more_helpful = db.Column(db.Integer, nullable=True)
    less_helpful = db.Column(db.Integer, nullable=True)
    recommend = db.Column(db.Boolean, nullable=True)
    review = db.Column(db.String(256), nullable=True)

    def __repr__(self):

        return f'<{self.__tablename__} {self.id} - {self.name}>'
    
    @classmethod
    def add(cls, id:str):
        """Documentation here
        """
        if not cls.id_exists(id):

            attr = cls(
                id=id
            )
            db.session.add(attr)
            db.session.commit()

            return attr
        
    @classmethod
    def id_exists(cls, id:int):
        r"""
        Documentation here
        """
        attr = cls.get(id=id)

        if attr:
            
            return True
        
        return False