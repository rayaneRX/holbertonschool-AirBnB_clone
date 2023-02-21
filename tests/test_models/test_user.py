import unittest

from models.user import User


class TestUser(unittest.TestCase):
    def test_user_email(self):
        user = User()
        user.email = "user@gmail.com"
        self.assertEqual(user.email, "user@gmail.com")

    def test_user_password(self):
        user = User()
        user.password = "mypass"
        self.assertEqual(user.password, "mypass")

    def test_user_first_name(self):
        user = User()
        user.first_name = "victor"
        self.assertEqual(user.first_name, "victor")

    def test_user_last_name(self):
        user = User()
        user.last_name = "Dubonus"
        self.assertEqual(user.last_name, "Dubonus")
