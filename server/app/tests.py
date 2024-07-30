import unittest
from app import create_app
from .models import db, User
from .configs import TestingConfig

class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestingConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    # def tearDown(self):
    #     db.session.remove()
    #     db.drop_all()
    #     self.app_context.pop()

    def test_password(self):
        u = User(username='ZIN', email='zin.it.dev@gmail.com')
        u.set_password('hello')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('hello'))
        

if __name__ == '__main__':
    unittest.main(verbosity=2)