from flask_restx import Resource, Namespace
from app.container import genre_service
from app.dao.model.genres import GenresSchema

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        result = GenresSchema(many=True).dump(genres)
        return result, 200


@genres_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = genre_service.get_one(gid)
        result = GenresSchema().dump(genre)
        return result, 200