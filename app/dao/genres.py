from app.dao.model.genres import Genres


class GenresDao:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        genres = Genres.query.all()
        return genres

    def get_one(self, gid):
        genre = Genres.query.get(gid)
        return genre