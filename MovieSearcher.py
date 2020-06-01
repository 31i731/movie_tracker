import tmdbsimple as tmdb
tmdb.API_KEY = '2f67f766f9080c17e2a3a1a2528d14c5'

class MovieSearcher:
    def __init__(self):
        pass

    def searchForMovie(self, title):
        search = tmdb.Search()
        return search.movie(query=title)
