from app.extensions.db import db


class Users(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.String(50), primary_key=True, unique=True)

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