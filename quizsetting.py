import tkinter as tk

# class Data:
#     def __init__(self, entry):
        # def add_question():
        #
        # def edit_question():
        #
        # def delete_question():
        #
        # def data_checking():


# def question_box():
#     messagebox.showinfo("Question", "Please fill in the question")
#
#
#
#
#
# def timer():


class QuestionSetting:
    def __init__(self, question_entry, a_entry, b_entry, c_entry, d_entry):
        self.question_entry = question_entry
        self.a_entry = a_entry
        self.b_entry = b_entry
        self.c_entry = c_entry
        self.d_entry = d_entry

    @classmethod
    def question_setting(cls):
        cls.question_entry = tk.Entry(font=('calibre', 10, 'normal'))
        cls.a_entry = tk.Entry(font=('calibre', 10, 'normal'))
        cls.b_entry = tk.Entry(font=('calibre', 10, 'normal'))
        cls.c_entry = tk.Entry(font=('calibre', 10, 'normal'))
        cls.d_entry = tk.Entry(font=('calibre', 10, 'normal'))


root = tk.Tk()

# creating a label for name using widget Label
name_label = tk.Label(text='Username', font=('calibre', 10, 'bold'))

# creating an entry for input
# name using widget Entry
# name_entry = tk.Entry(textvariable = name_label, font=('calibre', 10, 'normal'))



submit_button = tk.Button(root, text="Submit", command="login_page.login")

# Create Label widgets
label1 = tk.Label(root, text='Welcome to the quiz')
label2 = tk.Label(root, text='Please fill in the question', borderwidth=1, relief='solid')
label1.place(x=0, y=5)

#  Entry widgets
# question_entry = tk.Entry(root, font=('calibre', 10, 'normal'))
# a_entry = tk.Entry(root, font=('calibre', 10, 'normal'))
# b_entry = tk.Entry(root, font=('calibre', 10, 'normal'))
# c_entry = tk.Entry(root, font=('calibre', 10, 'normal'))
# d_entry = tk.Entry(root, font=('calibre', 10, 'normal'))




