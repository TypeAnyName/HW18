from app.dao.model.movies import Movies


class MoviesDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movies).get(mid)

    def get_all(self):
        movies = Movies.query.all()
        result = Movies.Schema(many=True).dump(movies)
        return result, 200