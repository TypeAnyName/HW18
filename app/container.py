from app.dao.directors import DirectorsDao
from app.dao.genres import GenresDao
from app.dao.movies import MoviesDao
from app.services.directors import DirectorsService
from app.services.genres import GenresService
from app.services.movies import MoviesService
from app.setup_db import db

movie_dao = MoviesDao(db.session)
movie_service = MoviesService(movies_dao=movie_dao)

director_dao = DirectorsDao(db.session)
director_service = DirectorsService(directors_dao=director_dao)

genre_dao = GenresDao(db.session)
genre_service = GenresService(genres_dao=genre_dao)