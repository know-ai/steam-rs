from .singleton import Singleton
import logging, os, ast, gzip
from logging.handlers import TimedRotatingFileHandler

def init_logging():
    r"""
    Documentation here
    """
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger('gunicorn').setLevel(logging.ERROR)
    logging.getLogger('engineio').setLevel(logging.ERROR)
    logging.getLogger('websockets.server').setLevel(logging.ERROR)
    logging.getLogger('websockets.protocol').setLevel(logging.ERROR)
    logging.basicConfig(level=logging.CRITICAL)
    handler = TimedRotatingFileHandler('logs/app.log', when='midnight', backupCount=365)
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.WARNING)


class Helpers:
    """
    Auxiliary functions
    """

    @staticmethod
    def exists(file: str)->bool:
        """
        Verify is a path or filename exists

        *Parameters*

        - **file:** (str) Path or Filename

        *Returns*

        - **exists:** (bool)
        """
        return os.path.exists(file)
    
    @classmethod
    def read(cls, filename: str, mode:str='r', source:str=None)->dict | list:
        """
        Reads file

        *Parameters*

        - *filename:* (str) Filename to read

        *Returns*

        - *file:* (dict | list | str) Content inside file
        """
        if cls.exists(filename):

            if source=="gzip":

                with gzip.open(filename, mode) as file:
                    
                    return [ast.literal_eval(line.strip()) for line in file]

            else:
            
                with open(filename, mode) as file:
                    
                    return [ast.literal_eval(line.strip()) for line in file]

        else:

            raise FileNotFoundError(f"{filename} not exists")