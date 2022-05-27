from app.dao.movies import MoviesDao


class MoviesService:
    def __init__(self, movies_dao: MoviesDao):
        self.movie_dao = movies_dao

    def get_all(self):
        return self.movie_dao.get_all()
