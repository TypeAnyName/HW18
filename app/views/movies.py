from flask_restx import Resource, Namespace

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        return "", 200

    def post(self):
        return "", 201
