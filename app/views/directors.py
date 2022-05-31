from flask_restx import Resource, Namespace
from app.container import director_service
from app.dao.model.directors import DirectorsSchema

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_all()
        result = DirectorsSchema(many=True).dump(directors)
        return result, 200


@directors_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_one(did)
        result = DirectorsSchema().dump(director)
        return result, 200
