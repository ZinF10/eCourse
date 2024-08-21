from app import create_app, db
from app.config import TestingConfig
from flask_testing import TestCase

class BaseTestCase(TestCase):
    def create_app(self):
        return create_app(TestingConfig)

    def setUp(self):
        self.app = self.create_app()
        db.create_all()
        
    # def tearDown(self):
    #     db.session.remove()
    #     db.drop_all()