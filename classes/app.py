from tkinter import *
from tkinter import messagebox

MAIN_COLOR = "#222831"


class AppUI():

    def __init__(self):
        super().__init__()
        self.bowler = Bowler()
        self.window = Tk()
        self.window.title("BracketBuddy")
        self.window.config(pady=50, padx=50, bg=MAIN_COLOR)
        self.window.geometry("800x500")
        self.window.resizable(True, True)
        self.checked = StringVar()
        self.checked.set("False")

        self.bowler_name_entry = Entry(width=30)
        self.bowler_avg_entry = Entry(width=30)
        self.bowler_num_brackets_entries = Entry(width=30)
        self.bowler_all_brackets_check = Checkbutton(text="All Brackets", bg=MAIN_COLOR, fg="#fff",
                                                     activebackground=MAIN_COLOR, variable=self.checked,
                                                     activeforeground="#fff", selectcolor=MAIN_COLOR,
                                                     onvalue="True", offvalue="False", command=self.if_all_brackets)

        self.bowler_name_label = Label(text="Bowler Name: ", bg=MAIN_COLOR, fg="white")
        self.bowler_avg_label = Label(text="Bowler's Average: ", bg=MAIN_COLOR, fg="white")
        self.bowler_num_brackets = Label(text="Number of Brackets: ", bg=MAIN_COLOR, fg="white")

        self.bowler_name_label.grid(column=1, row=2)
        self.bowler_name_entry.grid(column=2, row=2)
        self.bowler_avg_label.grid(column=1, row=3)
        self.bowler_avg_entry.grid(column=2, row=3)
        self.bowler_num_brackets.grid(column=1, row=4)
        self.bowler_num_brackets_entries.grid(column=2, row=4)
        self.bowler_all_brackets_check.grid(column=3, row=4)

        self.submit_btn = Button(text="Submit", command=self.add_bowlers)
        self.submit_btn.grid(column=2, row=6)

        self.bowler_name_entry.focus()

        self.window.mainloop()

    def add_bowlers(self):
        if self.bowler_avg_entry.get() == "":
            messagebox.showinfo("Average Missing", "Missing average, try again.")
        else:
            bowler_avg = int(self.bowler_avg_entry.get())
            bowler_name = self.bowler_name_entry.get()
            bowler_num_brackets = self.bowler_num_brackets_entries.get()
            all_brackets = self.checked.get()
            if bowler_num_brackets != "":
                bowler_num_brackets = int(self.bowler_num_brackets_entries.get())
            self.bowler.input_bowlers(bowler_name, bowler_avg, bowler_num_brackets, all_brackets)
            self.reset_fields()

    def reset_fields(self):
        self.bowler_name_entry.delete(0, END)
        self.bowler_avg_entry.delete(0, END)
        self.bowler_num_brackets_entries.delete(0, END)
        self.bowler_all_brackets_check.deselect()
        self.bowler_num_brackets_entries.config(state=NORMAL)
        self.bowler_name_entry.focus()

    def if_all_brackets(self):
        all_brackets = self.checked.get()
        if all_brackets == "True":
            self.bowler_num_brackets_entries.config(state=DISABLED)
        else:
            self.bowler_num_brackets_entries.config(state=NORMAL)
