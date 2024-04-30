from flask import Blueprint
from flask_restx import Api, Resource, fields

from backend.services.netflix import NetflixService

netflix_blueprint = Blueprint('Netflix', __name__)
netflix = Api(netflix_blueprint, title='Netflix API', description='This is the Netflix API')
netflix_ns = netflix.namespace('netflix', description='This is the Netflix Namespace')
netflix_model = netflix_ns.model('NetflixDescriptionModel', {
    'description': fields.String(required=True, description='The description of the film')
})


@netflix_ns.route('/films/<string:prefix_key>')
class NetflixResource(Resource):
    @netflix_ns.doc('List of expected films')
    @netflix_ns.marshal_list_with(netflix_model)
    def get(self, prefix_key):
        netflix_svc = NetflixService()
        return netflix_svc.get_films_by_prefix_description_key(prefix_key)
