import tkinter as tk
from tkinter import messagebox
from Page import *
from MovieSearcher import *
from DatabaseHandler import *
from hashlib import md5

class Register_Page(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        registration_form = tk.Frame(self)

        label_login = tk.Label(registration_form, text="Enter your new login:")
        label_login.grid(row = 0, column = 0, pady = 5, sticky = tk.W)

        self.log_in_name = tk.Entry(registration_form, width=30)
        self.log_in_name.grid(row = 1, column = 0)

        label_password = tk.Label(registration_form, text="Enter your new password:")
        label_password.grid(row = 2, column = 0, pady = (15, 2), sticky = tk.W)

        self.password = tk.Entry(registration_form, width=30, show="*")
        self.password.grid(row = 3, column = 0, pady = 1)

        label_repeat_password = tk.Label(registration_form, text="Repeat your password:")
        label_repeat_password.grid(row = 4, column = 0, pady = 5, sticky = tk.W)

        self.repeat_password = tk.Entry(registration_form, width=30, show="*")
        self.repeat_password.grid(row = 5, column = 0, pady = 1)

        label_display_name = tk.Label(registration_form, text="Enter your new display name:")
        label_display_name.grid(row = 6, column = 0, pady = (15, 5), sticky = tk.W)

        self.display_name = tk.Entry(registration_form, width=30)
        self.display_name.grid(row = 7, column = 0, pady = 1)

        registerBtn = tk.Button(registration_form, text="Register", command=self.registerNewUser)
        registerBtn.grid(row = 8, column = 0, pady = (8, 0), sticky = tk.W)

        registration_form.grid(row = 0, column = 0, pady = 10)

    def registerNewUser(self):
        databaseHandler = DatabaseHandler()
        conn = databaseHandler.establishConnection()
        c = databaseHandler.getCursor(conn)
        c.execute("SELECT login_name FROM users WHERE login_name=?", (self.log_in_name.get(),))
        row = c.fetchone()
        if row != None:
            messagebox.showerror("Error", "That login is already in use!")
            conn.close()
            return
        if self.password.get() != self.repeat_password.get():
            messagebox.showerror("Error", "The repeated password is not the same as your new password")
            conn.close()
            return
        hash_object = md5(self.password.get().encode())
        md5_password = hash_object.hexdigest()
        c.execute('''INSERT INTO users
                          (id, login_name, password, display_name) 
                           VALUES 
                          (?,?,?,?)''', (None, self.log_in_name.get(), md5_password, self.display_name.get()))
        conn.commit()
        messagebox.showinfo("Success", "You're successfully registered! Now you can log in!")
        conn.close()
