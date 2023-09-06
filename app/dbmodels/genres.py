from app.extensions.db import db


class Genres(db.Model):

    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), unique=True)

    def __repr__(self):

        return f'<{self.__tablename__} {self.id} - {self.name}>'
    
    @classmethod
    def add(cls, id:int, name:str):
        """Documentation here
        """
        if (not cls.id_exists(id) and not cls.name_exists(name)):

            attr = cls(
                id=id,
                name=name
            )
            db.session.add(attr)
            db.session.commit()

    @classmethod
    def name_exists(cls, name:str):
        r"""
        Documentation here
        """
        attr = cls.get(name=name)

        if attr:
            
            return True
        
        return False
    
    def id_exists(cls, id:int):
        r"""
        Documentation here
        """
        attr = cls.get(id=id)

        if attr:
            
            return True
        
        return False
