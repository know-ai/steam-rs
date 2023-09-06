import os
from ...helpers import Helpers

class ETL:
    """
    Helps you to do pipeline for Extraction - Transform and Load
    """

    def __init__(self):

        pass

    def read_json(self, filename: str)->dict | list:
        """
        Reads json file

        *Parameters*

        - *filename:* (str) Filename to read with or without .json extension

        *Returns*

        - *file:* (dict | list | str) Content inside file
        """
        ext = os.path.splitext(filename)[-1].lower()

        if ext != ".json":

            filename += ".json"

        return Helpers.read(filename)

    def read_gz(self, filename: str)->dict | list | str:
        """
        Reads file compressed into .gz extension

        *Parameters*

        - *filename:* (str) Filename to read with or without .gz extension

        *Returns*

        - *file:* (dict | list | str) Content inside file
        """
        ext = os.path.splitext(filename)[-1].lower()

        if ext != ".gz":

            filename += ".gz"

        return Helpers.read(filename, mode="rt", source="gzip")

    def run(self):
        """Documentaition here
        """
        pass