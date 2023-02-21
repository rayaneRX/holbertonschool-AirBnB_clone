from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

import unittest


class TestOtherBaseModelChildren(unittest.TestCase):
    def test_state(self):
        self.assertEqual("", State().name)

    def test_city(self):
        self.assertEqual("", City().name)

    def test_amenity(self):
        self.assertEqual("", City().name)

    def test_place(self):
        self.assertEqual("", Place().name)

    def test_review(self):
        self.assertEqual("", Review().text)
