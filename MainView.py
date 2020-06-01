import tkinter as tk

from page0 import *
from page1 import *
from page2 import *
from page3 import *
from page4 import *
from register_page import *
from login_page import *

from DatabaseHandler import *

import threading
from Page import Page

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p0 = Page0(self)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)
        register_page = Register_Page(self)
        self.login_page = Login_Page(self)
 
        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        
        container.pack(side="top", fill="both", expand=True)

        p0.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        register_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.login_page.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        self.b0 = tk.Button(buttonframe, text="Movie Searcher", command=p0.lift, state=tk.DISABLED)
        self.b1 = tk.Button(buttonframe, text="My Watched Movies", command=p1.loadAllWatchedMoviesAndLift, state=tk.DISABLED)
        self.b2 = tk.Button(buttonframe, text="Movies to watch", command=p2.loadAllToWatchMoviesAndLift, state=tk.DISABLED)
        self.b3 = tk.Button(buttonframe, text="Dropped movies", command=p3.loadAllDroppedMoviesAndLift, state=tk.DISABLED)
        self.b4 = tk.Button(buttonframe, text="Currently watching", command=p4.loadAllCurrentMoviesAndLift, state=tk.DISABLED)
        self.b5 = tk.Button(buttonframe, text="Register", command=register_page.lift)
        self.b6 = tk.Button(buttonframe, text="Log In", command=self.login_page.lift)

        self.b5.pack(side="left")
        self.b6.pack(side="left")
        self.b0.pack(side="left")
        self.b1.pack(side="left")
        self.b2.pack(side="left")
        self.b3.pack(side="left")
        self.b4.pack(side="left")

        #p0.show()

    def checkIfLoggedIn(self):
        if Page.loginedUser != (None,):
            self.enableBtns(self.b0, self.b1, self.b2, self.b3, self.b4)
        else:
            self.disableBtns(self.b0, self.b1, self.b2, self.b3, self.b4)
        threading.Timer(1.0, self.checkIfLoggedIn).start()

    def enableBtns(self, *btns):
        for btn in btns:
            btn['state'] = tk.NORMAL

    def disableBtns(self, *btns):
        for btn in btns:
            btn['state'] = tk.DISABLED

if __name__ == "__main__":

    databaseHandler = DatabaseHandler()
    databaseHandler.initAll()

    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.title("Movie Tracker")
    root.geometry("1150x500")
    warning = tk.Label(root, text="If you want to create and manage your lists of movies, you have to register and log in first!")
    warning.config(font=("Courier", 12))
    warning.pack()
    main.checkIfLoggedIn()
    root.mainloop()



