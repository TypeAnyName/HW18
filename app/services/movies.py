from app.dao.movies import MoviesDao


class MoviesService:
    def __init__(self, movies_dao: MoviesDao):
        self.movie_dao = movies_dao

    def get_all(self):
        return self.movie_dao.get_all()

    def get_one(self, mid):
        return self.movie_dao.get_one(mid)

    def get_by_year(self, year):
        return self.movie_dao.get_by_year(year)

    def get_by_genre(self, genre_id):
        return self.movie_dao.get_by_genre(genre_id)

    def get_by_director(self, director_id):
        return self.movie_dao.get_by_director(director_id)

    def create(self, data):
        self.movie_dao.create(data)

    def update(self, data, mid):
        movie = self.movie_dao.get_one(mid)

        movie.title = data["title"]
        movie.description = data['description']
        movie.trailer = data["trailer"]
        movie.year = data["year"]
        movie.rating = data["rating"]

        self.movie_dao.update(movie)

    def update_part(self, data, mid):
        movie = self.movie_dao.get_one(mid)

        if "title" in data:
            movie.title = data["title"]
        if 'description' in data:
            movie.description = data['description']
        if "trailer" in data:
            movie.trailer = data["trailer"]
        if "year" in data:
            movie.year = data["year"]
        if "rating" in data:
            movie.rating = data["rating"]

        self.movie_dao.update(movie)


    def delete(self, mid):
        movie = self.movie_dao.get_one(mid)
        self.movie_dao.delete(movie)
