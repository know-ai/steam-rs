from app.extensions.db import db


class BaseModel(db.Model):

    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), unique=True)

    def __repr__(self):

        return f'<{self.__tablename__} {self.id} - {self.name}>'
    
    @classmethod
    def add(cls, name:str):
        """Documentation here
        """
        if not cls.name_exists(name):

            attr = cls(
                name=name
            )
            db.session.add(attr)
            db.session.commit()

    @classmethod
    def get(cls, first=True, **fields):
        
        obj = cls.query.filter_by(**fields)

        if first:

            obj = obj.first()

        return obj

    @classmethod
    def name_exists(cls, name:str):
        r"""
        Documentation here
        """
        attr = cls.get(name=name)

        if attr:
            
            return True
        
        return False
    
    @classmethod
    def id_exists(cls, id:int):
        r"""
        Documentation here
        """
        attr = cls.get(id=id)

        if attr:
            
            return True
        
        return False