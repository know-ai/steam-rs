import unittest
from ..modules import ETL


class TestETL(unittest.TestCase):
    r"""
    Documentation here
    """

    def setUp(self) -> None:

        pass

    def test_read_json(self):
        """
        Verify read_json function works correctly
        """
        etl = ETL()
        filename = "app/tests/data/australian_user_reviews.json"
        data = etl.read_json(filename)
        first_item = {
            'user_id': '76561197970982479', 
            'user_url': 'http://steamcommunity.com/profiles/76561197970982479', 
            'reviews': [
                {
                    'funny': '', 
                    'posted': 'Posted November 5, 2011.', 
                    'last_edited': '', 
                    'item_id': '1250', 
                    'helpful': 'No ratings yet', 
                    'recommend': True, 
                    'review': 'Simple yet with great replayability. In my opinion does "zombie" hordes and team work better than left 4 dead plus has a global leveling system. Alot of down to earth "zombie" splattering fun for the whole family. Amazed this sort of FPS is so rare.'
                }, 
                {
                    'funny': '', 
                    'posted': 'Posted July 15, 2011.', 
                    'last_edited': '', 
                    'item_id': '22200', 
                    'helpful': 'No ratings yet', 
                    'recommend': True, 
                    'review': "It's unique and worth a playthrough."
                }, 
                {
                    'funny': '', 
                    'posted': 'Posted April 21, 2011.', 
                    'last_edited': '', 
                    'item_id': '43110', 
                    'helpful': 'No ratings yet', 
                    'recommend': True, 
                    'review': 'Great atmosphere. The gunplay can be a bit chunky at times but at the end of the day this game is definitely worth it and I hope they do a sequel...so buy the game so I get a sequel!'
                }
            ]
        }
        with self.subTest(f"Checking First Item"):
            
            self.assertDictEqual(data[0], first_item)

        last_item = {
            'user_id': 'LydiaMorley', 
            'user_url': 'http://steamcommunity.com/id/LydiaMorley', 
            'reviews': [
                {
                    'funny': '1 person found this review funny', 
                    'posted': 'Posted July 3.', 
                    'last_edited': '', 
                    'item_id': '273110', 
                    'helpful': '1 of 2 people (50%) found this review helpful', 
                    'recommend': True, 
                    'review': 'had so much fun plaing this and collecting resources xD we won on my first try and killed final boss!'
                }, 
                {
                    'funny': '', 
                    'posted': 'Posted July 20.', 
                    'last_edited': '', 
                    'item_id': '730', 
                    'helpful': 'No ratings yet', 
                    'recommend': True, 
                    'review': ':D'
                }, 
                {
                    'funny': '', 
                    'posted': 'Posted July 2.', 
                    'last_edited': '', 
                    'item_id': '440', 
                    'helpful': 'No ratings yet', 
                    'recommend': True, 
                    'review': 'so much fun :D'
                }
            ]
        }

        with self.subTest(f"Checking Last Item"):
            
            self.assertDictEqual(data[-1], last_item)


    def test_read_gz(self):
        """
        Verify read_gz function works correctly
        """
        etl = ETL()
        filename = "app/tests/data/user_reviews.json.gz"
        data = etl.read_gz(filename)
        first_item = {
            'user_id': '76561197970982479', 
            'user_url': 'http://steamcommunity.com/profiles/76561197970982479', 
            'reviews': [
                {
                    'funny': '', 
                    'posted': 'Posted November 5, 2011.', 
                    'last_edited': '', 
                    'item_id': '1250', 
                    'helpful': 'No ratings yet', 
                    'recommend': True, 
                    'review': 'Simple yet with great replayability. In my opinion does "zombie" hordes and team work better than left 4 dead plus has a global leveling system. Alot of down to earth "zombie" splattering fun for the whole family. Amazed this sort of FPS is so rare.'
                }, 
                {
                    'funny': '', 
                    'posted': 'Posted July 15, 2011.', 
                    'last_edited': '', 
                    'item_id': '22200', 
                    'helpful': 'No ratings yet', 
                    'recommend': True, 
                    'review': "It's unique and worth a playthrough."
                }, 
                {
                    'funny': '', 
                    'posted': 'Posted April 21, 2011.', 
                    'last_edited': '', 
                    'item_id': '43110', 
                    'helpful': 'No ratings yet', 
                    'recommend': True, 
                    'review': 'Great atmosphere. The gunplay can be a bit chunky at times but at the end of the day this game is definitely worth it and I hope they do a sequel...so buy the game so I get a sequel!'
                }
            ]
        }
        
        with self.subTest(f"Checking First Item"):
            
            self.assertDictEqual(data[0], first_item)

        last_item = {
            'user_id': 'LydiaMorley', 
            'user_url': 'http://steamcommunity.com/id/LydiaMorley', 
            'reviews': [
                {
                    'funny': '1 person found this review funny', 
                    'posted': 'Posted July 3.', 
                    'last_edited': '', 
                    'item_id': '273110', 
                    'helpful': '1 of 2 people (50%) found this review helpful', 
                    'recommend': True, 
                    'review': 'had so much fun plaing this and collecting resources xD we won on my first try and killed final boss!'
                }, 
                {
                    'funny': '', 
                    'posted': 'Posted July 20.', 
                    'last_edited': '', 
                    'item_id': '730', 
                    'helpful': 'No ratings yet', 
                    'recommend': True, 
                    'review': ':D'
                }, 
                {
                    'funny': '', 
                    'posted': 'Posted July 2.', 
                    'last_edited': '', 
                    'item_id': '440', 
                    'helpful': 'No ratings yet', 
                    'recommend': True, 
                    'review': 'so much fun :D'
                }
            ]
        }

        with self.subTest(f"Checking Last Item"):
            
            self.assertDictEqual(data[-1], last_item)