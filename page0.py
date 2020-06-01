import tkinter as tk
from Page import *
from MovieSearcher import *
from DatabaseHandler import *

class Page0(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.movieSearcher = MovieSearcher()
        self.selectedMovie = None

        self.moviesOverviews = []
        self.moviesPosters = []

        searchFrame = tk.Frame(self)

        label0 = tk.Label(searchFrame, text="Enter a movie you want to find...")
        label0.grid(row = 0, column = 0)

        self.entryForMovie = tk.Entry(searchFrame, width=30)
        self.entryForMovie.grid(row = 1, column = 0, pady = 5)

        searchButton = tk.Button(searchFrame, text="Search", command=self.fillTheList)
        searchButton.grid(row = 2, column = 0, sticky = tk.W, pady = 5)

        searchFrame.grid(row = 0, column = 0, pady = 10)

        moviesFrame = tk.Frame(self)
        self.listOfMovies = tk.Listbox(moviesFrame, width=60)
        self.listOfMovies.grid(row = 0, column = 0)
        self.listOfMovies.bind('<<ListboxSelect>>', self.onselect)

        btnsFrame = tk.Frame(moviesFrame)
        markAsWatchedBtn = tk.Button(btnsFrame, text="Mark as watched", command=self.markAsWatched)
        markAsWatchedBtn.grid(row = 0, column = 0, pady = (15, 0), sticky=tk.W)

        markAsToWatchBtn = tk.Button(btnsFrame, text="Mark as 'to watch'", command=self.markAsToWatch)
        markAsToWatchBtn.grid(row = 0, column = 1, pady = (15, 0), sticky=tk.W)

        markAsDroppedBtn = tk.Button(btnsFrame, text="Mark as 'Dropped'", command=self.markAsDropped)
        markAsDroppedBtn.grid(row = 0, column = 2, pady = (15, 0), sticky=tk.W)

        markAsWatchingBtn = tk.Button(btnsFrame, text="Mark as 'Currently watching'", command=self.markAsWatching)
        markAsWatchingBtn.grid(row = 1, column = 0, columnspan=2 ,pady = (5, 0), sticky=tk.W)

        btnsFrame.grid(row=1, column = 0, sticky=tk.W)
        moviesFrame.grid(row = 0, column = 1, pady = (40,0))
    
        self.synopsisText = tk.Text(self, width=45)
        self.synopsisText.grid(row = 0, column = 2, pady = 20, padx = 15)
        
    def fillTheList(self):
        response = self.movieSearcher.searchForMovie(self.entryForMovie.get())
        self.listOfMovies.delete(0,tk.END)
        self.moviesOverviews = []
        self.moviesPosters = []
        for r in response['results']:
            print(r)
            print(f"{r['id']}: {r['title']}")
            self.listOfMovies.insert(tk.END, f"{r['title']} ({r['release_date']})")
            self.moviesOverviews.append(r['overview'])
            self.moviesPosters.append(r['poster_path'])

    def markAsWatched(self):
        databaseHandler = DatabaseHandler()
        conn = databaseHandler.establishConnection()
        c = databaseHandler.getCursor(conn)
        c.execute(''' INSERT INTO users_movies(user_id,movie,favourite,score,status,poster_path)
              VALUES(?,?,?,?,?,?) ''', (Page.loginedUser[0],self.selectedMovie[1],0,0,"watched",self.moviesPosters[self.selectedMovie[0]]))
        conn.commit()
        conn.close()

    def markAsToWatch(self):
        databaseHandler = DatabaseHandler()
        conn = databaseHandler.establishConnection()
        c = databaseHandler.getCursor(conn)
        c.execute(''' INSERT INTO users_movies(user_id,movie,favourite,score,status,poster_path)
              VALUES(?,?,?,?,?,?) ''', (Page.loginedUser[0],self.selectedMovie[1],0,0,"to_watch",self.moviesPosters[self.selectedMovie[0]]))
        conn.commit()
        conn.close()

    def markAsDropped(self):
        databaseHandler = DatabaseHandler()
        conn = databaseHandler.establishConnection()
        c = databaseHandler.getCursor(conn)
        c.execute(''' INSERT INTO users_movies(user_id,movie,favourite,score,status,poster_path)
              VALUES(?,?,?,?,?,?) ''', (Page.loginedUser[0],self.selectedMovie[1],0,0,"dropped",self.moviesPosters[self.selectedMovie[0]]))
        conn.commit()
        conn.close()

    def markAsWatching(self):
        databaseHandler = DatabaseHandler()
        conn = databaseHandler.establishConnection()
        c = databaseHandler.getCursor(conn)
        c.execute(''' INSERT INTO users_movies(user_id,movie,favourite,score,status,poster_path)
              VALUES(?,?,?,?,?,?) ''', (Page.loginedUser[0],self.selectedMovie[1],0,0,"watching",self.moviesPosters[self.selectedMovie[0]]))
        conn.commit()
        conn.close()

    def onselect(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.selectedMovie = (index,value)
        self.synopsisText.delete('1.0', tk.END)
        self.synopsisText.insert(tk.INSERT, self.moviesOverviews[index])
