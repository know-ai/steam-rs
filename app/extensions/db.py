from app.helpers import Singleton
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


class DB(Singleton):

    def __init__(self):
        
        self.app = None

    def init_app(self, app):
        r"""
        Documentation here
        """
        db.init_app(app)
    
        Migrate(app, db)

        return app