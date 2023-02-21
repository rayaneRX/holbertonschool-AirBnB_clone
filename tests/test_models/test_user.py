import unittest

from models.user import User


class TestUser(unittest.TestCase):
    def test_user_email(self):
        user = User()
        user.email = "user@gmail.com"
        self.assertNotEqual(user.email, User.email)

    def test_user_password(self):
        user = User()
        user.password = "mypass"
        self.assertNotEqual(user.password, User.password)

    def test_user_first_name(self):
        user = User()
        user.first_name = "victor"
        self.assertNotEqual(user.first_name, User.first_name)

    def test_user_last_name(self):
        user = User()
        user.last_name = "Dubonus"
        self.assertNotEqual(user.last_name, User.last_name)
