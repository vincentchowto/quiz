import tkinter as tk
import sqlite3

# Function to submit data to SQLite database
def submit_data():
    user_input = entry.get()
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c. execute('''CREATE TABLE IF NOT EXISTS entries(
               id INTEGER PRIMARY KRY,
               data TEXT
                )''')
    c.execute("INSERT INTO entries(data) VALUES (?)", (user_input))
    conn.commit()
    conn.close()
    print("Data submitted and saved to database:",user_input)

# Create the main window
root=tk.Tk()
# root.title("Entry Widget with SQLite Database")

#Create an Entry Widget
entry=tk.Entry(root)
# entry.pack(pady=10)

#Create a button to submit the data
submit_button=tk