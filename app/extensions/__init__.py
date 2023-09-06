from .db import DB
from .api import Api
from .cors import Cors

_db = DB()
_api = Api()
_cors = Cors()

def init_app(app):
    """
    Application extensions initialization.
    """
    extensions = (_db, _api, _cors )

    for extension in extensions:
        
        extension.init_app(app)