import tkinter as tk
from Page import *
from MovieSearcher import *
from DatabaseHandler import *
import urllib3
from PIL import ImageTk, Image
import io

class Page4(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.moviesPosters = []

        frameList = tk.Frame(self)

        self.listbox = tk.Listbox(frameList, width=60)
        self.listbox.grid(row=0, column=0)
        self.listbox.bind('<<ListboxSelect>>', self.onselect)

        frameList.grid(row = 0, column = 0, pady = (20,0), padx = (25,0), sticky=tk.N)

    def loadAllCurrentMoviesAndLift(self):
        databaseHandler = DatabaseHandler()
        conn = databaseHandler.establishConnection()
        c = databaseHandler.getCursor(conn)
        c.execute("SELECT * FROM users_movies WHERE user_id=? AND status='watching'", (Page.loginedUser[0],))
        rows = c.fetchall()
        print(rows)
        conn.close()
        self.listbox.delete(0, tk.END)
        self.moviesPosters = []
        for r in rows:
            self.listbox.insert(tk.END, r[1])
            self.moviesPosters.append(r[5])
        self.show()

    def onselect(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])

        http = urllib3.PoolManager()

        url = f'http://image.tmdb.org//t//p//w300/{self.moviesPosters[index]}'
        response = http.request('GET', url)

        im = Image.open(io.BytesIO(response.data))
        image = ImageTk.PhotoImage(im)
        label1 = tk.Label(self, image=image)
        label1.photo = image
        label1.grid(row=0, column=1, pady=(20,0), padx=(20,0))
