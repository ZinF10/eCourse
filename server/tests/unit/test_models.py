from app.models import User
from tests.conftest import BaseTestCase

class ModelsUnitTest(BaseTestCase):
    def test_password(self):
        u = User(username='ZIN', email='zin.it.dev@gmail.com', password="hello")
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('hello'))