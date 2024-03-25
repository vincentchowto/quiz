import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import loginpage
from quizsetting import QuestionSetting
import ImportSQL

# Main window:
root = tk.Tk()
root.title("Quiz")
root.geometry('640x480')

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl, width=640, height=480)
tab2 = ttk.Frame(tabControl, width=640, height=480)
tab3 = ttk.Frame(tabControl, width=640, height=480)

tabControl.add(tab1, text='Login')
tabControl.add(tab2, text='Quiz')
tabControl.add(tab3, text="Database")
tabControl.grid(row=0, column=0, padx=0, pady=0, sticky='NW')

# Tab 1
login_page = loginpage.Login(loginpage.username_var, loginpage.passw_var)

username_label = tk.Label(tab1, text='Username:')
password_label = tk.Label(tab1, text='Password:')
username_label.grid(column=0, row=0, padx=10, pady=10)
password_label.grid(column=0, row=1, padx=10, pady=10)

username_entry = tk.Entry(tab1, textvariable=loginpage.username_var, show='*')
password_entry = tk.Entry(tab1, textvariable=loginpage.passw_var, show='*')
username_entry.grid(row=0, column=1, padx=10, pady=10)
password_entry.grid(row=1, column=1, padx=10, pady=10)

login_button = tk.Button(tab1, text="Login", command=loginpage.Login)
login_button.grid(row=2, column=1, padx=10, pady=10)

# Tab 2
question_label = tk.Label(tab2,textvariable='QuestionSetting.question_label')
a_label = tk.Label(tab2, text='Option A:')
b_label = tk.Label(tab2, text='Option B:')
c_label = tk.Label(tab2, text='Option C:')
d_label = tk.Label(tab2, text='Option D:')

question_label.grid(column=0, row=0, padx=10, pady=10)
a_label.grid(column=0, row=1, padx=10, pady=10)
b_label.grid(column=0, row=2, padx=10, pady=10)
c_label.grid(column=0, row=3, padx=10, pady=10)
d_label.grid(column=0, row=4, padx=10, pady=10)

question_setting = QuestionSetting(quizsetting.question_entry, a_entry, b_entry, c_entry, d_entry)
QuestionSetting.question_entry.grid(row=1, column=1, padx=10, pady=10)
QuestionSetting.a_entry.grid(row=1, column=1, padx=10, pady=10)
QuestionSetting.b_entry.grid(row=2, column=1, padx=10, pady=10)
QuestionSetting.c_entry.grid(row=3, column=1, padx=10, pady=10)
QuestionSetting.d_entry.grid(row=4, column=1, padx=10, pady=10)

root.mainloop()




