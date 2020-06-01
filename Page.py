import tkinter as tk

class Page(tk.Frame):
    loginedUser = (None,)
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.grid_columnconfigure(0, minsize=250)

    def show(self):
        self.lift()
