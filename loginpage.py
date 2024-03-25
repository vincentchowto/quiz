import tkinter as tk

class Login:
    def __init__(self, username_var, passw_var):
        self.username_var = username_var
        self.passw_var = passw_var

    def login(self):
        username = self.username_var.get()
        password = self.passw_var.get()

        print("The name is:", username)
        print("The password is:", password)

        self.username_var.set("")
        self.passw_var.set("")



# Create variables for username and password entry
root = tk.Tk()
username_var = tk.StringVar(master=root)
passw_var = tk.StringVar(master=root)






