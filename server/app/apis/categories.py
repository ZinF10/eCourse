from ..dao import load_categories
from flask_restx import Resource
from .dto import category_api, category
from ..services.caching import cache

@category_api.route('/')
class CategoryListResource(Resource):
    @cache.cached(timeout=60)
    @category_api.marshal_with(category, code=200, as_list=True)
    def get(self):
        """ Get all categories """
        return load_categories()