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
                "review": """
I've always liked games like Terraria with the 2 dimensional survival 
and exploration aspect and Starbound does all these well and MORE!
Lets start with its soundtrack: To sum it up in one paragraph would do it injustice. 
This games soundtrack is fully orchestral and imersive. 
The music just fits perfectly where-ever you are in game. 
Whether you are spelunking or just flying through the vast expanse of space it 
fits perfectly and leaves you in awe.Ok onto the graphics: 
The look and feel of this game bring the vast worlds to life with the many colors 
and alien dirts, trees and the mixture of monsters. 
The backgrounds of the planets match up the the foregrounds well 
and give the 2d aspect that 3d feel.Now the gameplay: 
Starbound has a nice rich layer of gameplay revolving around survival. 
In the latest unstable build updates they have introduced a very needed layer 
of missions and npc quests which fullfil the gaps of just flying from planet 
to planet and give purpose.Starbounds worlds have a wide variety of random aspects to 
them.First off the flora: Flora of planets consists of 2-3 main aspects. 
The Trees, the small bushes and medium bushes. 
Each planet has a vast difference to the next in their flora with trees coming 
in 2-3 different types from metallic trees to plain out alien tentacles.
Now onto the fauna: Each planet has 3 or more ground based animals which increase 
in strength further beneath the planets surface. 
Starbound has a feature where animals are customized via their limbs and body. 
There are many arms, legs, feet and bodies all just jumbled to together from monster to 
monster making cute monsters and just plain out terrifying ones. 
There are also around 2 bird species per planet. Using the same general system.
I personally suggest this game because of its deep and fluid experience and its 
wide modding community.8-9/10 for an early access and its only going to get better!
""",
                "posted": "2014-06-07"
            }
            obj = Reviews.add(**review)

            self.assertDictEqual(dict(sorted(obj.serialize().items())), dict(sorted(review.items())))