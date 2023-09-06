import os
from flask import Flask
from dotenv import load_dotenv
import os
from config import DevelopmentConfig, ProductionConfig
from app.dbmodels import *


app = Flask(__name__, instance_relative_config=False)

def load_env_var():
    r"""
    Documentation here
    """
    load_dotenv()
    mode = os.environ.get('APP_MODE') or 'Development'
    port = int(os.environ.get('APP_PORT') or '5004')

    return mode, port

mode, port = load_env_var()
if mode.lower() == 'development':
    app.config.from_object(DevelopmentConfig)
else:
    app.config.from_object(ProductionConfig)


class CreateApp():
    """Initialize the core application."""

    def __call__(self):
        """
        Documentation here
        """
        self.application = app

        with app.app_context():

            from . import extensions
            _app = extensions.init_app(app)

            from . import modules
            _app = modules.init_app(app)

            return _app