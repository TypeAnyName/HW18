from flask_restx import Resource, Namespace

from app.container import movie_service
from app.dao.model.movies import Movies, MoviesSchema

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = movie_service.get_all()
        result = MoviesSchema(many=True).dump(movies)
        return result, 200

    # def post(self):
    #     return "", 201
