import unittest
from ..helpers import Helpers

class TestHelpers(unittest.TestCase):
    r"""
    Cases suite to test Helpers class
    """

    def setUp(self) -> None:

        pass

    def test_file_exists(self):
        """
        Verify if exists function works correctly
        """
        filename = "app/tests/data/steam_games.json.gz"
        
        with self.subTest(f"Checking {filename}"):
            
            self.assertTrue(Helpers.exists(filename))

        filename = "app/tests/data/user_reviews.json.gz"
        
        with self.subTest(f"Checking {filename}"):
            
            self.assertTrue(Helpers.exists(filename))

        filename = "app/tests/data/users_items.json.gz"
        
        with self.subTest(f"Checking {filename}"):
            
            self.assertTrue(Helpers.exists(filename))

    def test_file_not_exists(self):
        """
        Verify if exists function works correctly
        """
        filename = "app/tests/data/steam_games.json"
        self.assertFalse(Helpers.exists(filename))
