import tkinter as tk
from tkinter import messagebox
from Page import *
from MovieSearcher import *
from DatabaseHandler import *
from hashlib import md5

class Login_Page(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        login_form = tk.Frame(self)
        
        label_login = tk.Label(login_form, text="Enter your login:")
        label_login.grid(row = 0, column = 0, pady = 5, sticky = tk.W)

        self.log_in_name = tk.Entry(login_form, width=30)
        self.log_in_name.grid(row = 1, column = 0)

        label_password = tk.Label(login_form, text="Enter your password:")
        label_password.grid(row = 2, column = 0, pady = (15, 2), sticky = tk.W)

        self.password = tk.Entry(login_form, width=30, show="*")
        self.password.grid(row = 3, column = 0, pady = 1)

        loginBtn = tk.Button(login_form, text="Log in", command=self.login)
        loginBtn.grid(row = 4, column = 0, pady = (8, 0), sticky = tk.W)

        login_form.grid(row = 0, column = 0, pady = 10)

    def login(self):
        databaseHandler = DatabaseHandler()
        conn = databaseHandler.establishConnection()
        c = databaseHandler.getCursor(conn)
        hash_object = md5(self.password.get().encode())
        md5_password = hash_object.hexdigest()
        c.execute("SELECT * FROM users WHERE login_name=? AND password=?", (self.log_in_name.get(),md5_password))
        row = c.fetchone()
        print(row)
        if row == None:
            messagebox.showerror("Error", "Wrong login or password")
            Page.loginedUser = (None,)
            conn.close()
            return

        messagebox.showinfo("Success", "You're successfully login'd! Now you can create your lists!")
        Page.loginedUser = row
        conn.close()

    def enable_buttons(self, *btns):
        for btn in btns:
            btn['state'] = tk.NORMAL
