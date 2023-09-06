import unittest
from app.extensions.db import db
from app.dbmodels import Publishers, Developers, Genres, Specs, Tags
from app import app

class TestDB(unittest.TestCase):
    r"""
    Documentation here
    """
    def setUp(self) -> None:
        with app.app_context():
    
            db.create_all()
            return super().setUp()

    def tearDown(self):
        """
        Ensures that the database is emptied for next unit test
        """
        with app.app_context():
            
            db.drop_all()

    def test_db_creation(self):
        """
        Ensures that database is created with the correct scheme
        """
        tables = sorted([
            'publishers',
            'developers',
            'tags',
            'specs',
            'genres',
            'games'
        ])
        assert_tables = sorted(list(db.metadata.tables.keys()))
        self.assertListEqual(tables, assert_tables)

    def test_add_publisher(self):
        """
        Ensures that publisher is added into publishers table
        """
        publisher = {
            "name": "Yacht Club Games"
        }
        with app.app_context():
            Publishers.add(**publisher)
            pub = Publishers.get(name=publisher['name'])
            self.assertDictEqual({
                "name": pub.name
            }, publisher)

    def test_add_developer(self):
        """
        Ensures that developer is added into developers table
        """
        developer = {
            "name": "Eisenbahnwerk"
        }
        with app.app_context():
            Developers.add(**developer)
            pub = Developers.get(name=developer['name'])
            self.assertDictEqual({
                "name": pub.name
            }, developer)

    def test_add_genre(self):
        """
        Ensures that genre is added into genres table
        """
        genre = {
            "name": "Simulation"
        }
        with app.app_context():
            Genres.add(**genre)
            pub = Genres.get(name=genre['name'])
            self.assertDictEqual({
                "name": pub.name
            }, genre)

    def test_add_tag(self):
        """
        Ensures that tag is added into tags table
        """
        tag = {
            "name": "Strategy"
        }
        with app.app_context():
            Tags.add(**tag)
            pub = Tags.get(name=tag['name'])
            self.assertDictEqual({
                "name": pub.name
            }, tag)

    def test_add_spec(self):
        """
        Ensures that spec is added into specs table
        """
        spec = {
            "name": "Single-Player"
        }
        with app.app_context():
            Specs.add(**spec)
            pub = Specs.get(name=spec['name'])
            self.assertDictEqual({
                "name": pub.name
            }, spec)