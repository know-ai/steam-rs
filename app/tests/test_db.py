import unittest
from app.extensions.db import db
from app.dbmodels import Publishers, Developers, Genres, Specs, Tags, Games, Users, Reviews
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
            'games_specs',
            'users',
            'reviews',
            'funny_reviews',
            'helpful_reviews'
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
            game['genres'] = genres
            game['tags'] = tags
            game['specs'] = specs
            game["url"] = f"http://store.steampowered.com/app/{obj.id}/{obj.name}/"
            self.assertDictEqual(dict(sorted(obj.serialize().items())), dict(sorted(game.items())))

    def test_add_user(self):
        """
        Ensures that user is added into users table
        """
        user = {
            "id": "xfluttersx",
            "steam_id": "76561198069920369"
        }

        with app.app_context():

            Users.add(**user)
            obj = Users.get(id=user['id'])
            self.assertDictEqual({
                "id": obj.id,
                "steam_id": obj.steam_id
            }, user)

    def test_add_review(self):
        """
        Ensures that review is added into reviews table
        """
        user = {
            "id": "xfluttersx",
            "steam_id": "76561198069920369"
        }
        with app.app_context():

            Users.add(**user)
            user_obj = Users.get(id=user['id'])

            review = {
                "user_id": user_obj.id,
                "recommend": True,
                "review": "This Game Doesn't Work",
                "posted": "2014-06-07"
            }
            obj = Reviews.add(**review)

            self.assertDictEqual(dict(sorted(obj.serialize().items())), dict(sorted(review.items())))

    def test_add_funny_review(self):
        """
        Ensures that funny is added into funny_reviews table
        """
        users = [
            {
                "id": "devvonst",
                "steam_id": "76561198069920369"
            },
            {
                "id": "Carlos",
                "steam_id": "82385888455000"
            }
        ]
        with app.app_context():
            
            for user in users:
                
                Users.add(**user)

            review = {
                "user_id": user["id"],
                "recommend": False,
                "review": "This Game Doesn't Work",
                "posted": "2014-06-07"
            }
            obj_review = Reviews.add(**review)

            funny_review = {
                "funny": True,
                "review": obj_review
            }
            obj_user = Users.get(id=users[0]['id'])
            obj_user.vote_for_funny_review(**funny_review)
            for obj in obj_user.funny_reviews:
                
                with self.subTest("Valid funny_review"): 
                    
                    result_assert = {
                        "id": 1,
                        "user_id": users[0]["id"]
                    }

                    result_assert.update(**funny_review)
                    result_assert["review"] = review

                    self.assertDictEqual(dict(sorted(obj.serialize().items())), dict(sorted(result_assert.items())))
            
            with self.subTest("Same user can't vote itself by funny review"):

                obj_user = Users.get(id=users[1]['id'])
                self.assertEqual(obj_user.vote_for_funny_review(**funny_review), None)

    def test_add_helpful_review(self):
        """
        Ensures that helpful is added into helpful_reviews table
        """
        pass
