from flask_restx import Resource, Namespace
from flask import request, jsonify
from app.container import movie_service
from app.dao.model.movies import Movies, MoviesSchema

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):

        year = request.args.get('year')
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        if year:
            movies = movie_service.get_by_year(year).all()
        elif director_id:
            movies = movie_service.get_by_director(director_id).all()
        elif genre_id:
            movies = movie_service.get_by_genre(genre_id).all()
        else:
            movies = movie_service.get_all()

        result = MoviesSchema(many=True).dump(movies)
        return result, 200

    def post(self):
        data = request.get_json()
        movies_id = data["id"]
        movie_service.create(data)
        response = jsonify()
        response.status_code = 201
        response.headers['location'] = f'/{movies_id}'
        return response


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        result = MoviesSchema().dump(movie)
        return result, 200

    def put(self, mid):
        data = request.get_json()
        movie_service.update(data, mid)
        return '', 204

    def patch(self, mid):
        data = request.get_json()
        movie_service.update_part(data, mid)
        return '', 204

    def delete(self, mid):
        movie_service.delete(mid)
        return '', 204


