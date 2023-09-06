import unittest
from app.extensions.db import db
from app.dbmodels import Publishers, Developers, Genres, Specs, Tags, Games
from app import app

DATE_FORMAT = "%Y-%m-%d"

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
            'games',
            'games_genres',
            'games_tags',
            'games_specs'
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
            obj = Publishers.get(name=publisher['name'])
            self.assertDictEqual({
                "name": obj.name
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
            obj = Developers.get(name=developer['name'])
            self.assertDictEqual({
                "name": obj.name
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
            obj = Genres.get(name=genre['name'])
            self.assertDictEqual({
                "name": obj.name
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
            obj = Tags.get(name=tag['name'])
            self.assertDictEqual({
                "name": obj.name
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
            obj = Specs.get(name=spec['name'])
            self.assertDictEqual({
                "name": obj.name
            }, spec)

    def test_add_game(self):
        """
        Ensures that game is added into games table
        """
        game = {
            "id": 562500,
            "title": "Warstone TD",
            "name": "Warstone TD",
            "price": 14.99,
            "release_date": "2017-04-06",
            "discount_price": None,
            "publisher": "Battlecruiser Games",
            "developer": "Battlecruiser Games",
            "early_access": True,
            "metascore": None
        }
        with app.app_context():
            # Create pusblisher record
            publisher = {
                "name": game["publisher"]
            }
            Publishers.add(**publisher)
            # Create developer record
            developer = {
                "name": game["developer"]
            }
            Developers.add(**developer)
            # Create game record
            Games.add(**game)
            obj = Games.get(id=game['id'])
            # Add Genres to game
            genres = ["Indie", "Strategy", "Early Access"]
            obj.add_genres(*genres)
            # Add Tags to game
            tags = [
                "Early Access", 
                "Strategy", 
                "Indie", 
                "Tower Defense", 
                "Co-op", 
                "Fantasy", 
                "PvP", 
                "Multiplayer", 
                "Story Rich", 
                "Great Soundtrack", 
                "RTS"
            ]
            obj.add_tags(*tags)
            # Add Specs to game
            specs = [
                "Single-player",
                "Online Multi-Player",
                "Online Co-op",
                "Steam Achievements",
                "Steam Trading Cards"
            ]
            obj.add_specs(*specs)
            # Test
            result = {
                "id": obj.id,
                "title": obj.title,
                "name": obj.name,
                "price": obj.price,
                "release_date": obj.release_date.date().strftime(DATE_FORMAT),
                "discount_price": obj.discount_price,
                "publisher": obj.publisher.name,
                "developer": obj.developer.name,
                "early_access": obj.early_access,
                "metascore": obj.metascore,
                "genres": [genre.name for genre in obj.genres],
                "tags": [tag.name for tag in obj.tags],
                "specs": [spec.name for spec in obj.specs]
            }
            game['genres'] = genres
            game['tags'] = tags
            game['specs'] = specs
            self.assertDictEqual(dict(sorted(result.items())), dict(sorted(game.items())))