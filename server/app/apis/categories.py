from ..dao import load_categories
from flask_restx import Resource
from .serializers import category_api, category

@category_api.route('/')
class CategoryListResource(Resource):
    @category_api.marshal_with(category, code=200, as_list=True)
    def get(self):
        """ Get all categories """
        return load_categories()