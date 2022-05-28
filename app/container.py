from app.dao.movies import MoviesDao
from app.services.movies import MoviesService
from app.setup_db import db

movie_dao = MoviesDao(db.session)
movie_service = MoviesService(movies_dao=movie_dao)
