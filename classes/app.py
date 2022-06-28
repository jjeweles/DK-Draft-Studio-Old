from tkinter import *
from tkinter import messagebox, ttk

MAIN_COLOR = "#ddd"
DARK_BLUE = "#2d3142"
LIGHT_GREY = "#bfc0c0"
WHITE = "#fff"
ORANGE = "#ef8354"
LIGHT_BLUE = "#4f5d75"
BLACK = "#000"


class AppUI:

    def __init__(self):
        super().__init__()
        self.window = Tk()
        self.window.title("DK Draft Studio")
        self.window.config(pady=10, padx=10, bg=DARK_BLUE)
        self.window.geometry("1024x768")
        self.window.resizable(True, True)

        notebook = ttk.Notebook(self.window)
        notebook.pack(fill=BOTH, expand=1)

        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("TNotebook", background=DARK_BLUE, borderwidth=0)
        self.style.configure("TNotebook.Tab", background=ORANGE, foreground=BLACK, borderwidth=0)
        self.style.configure("Tab", focuscolor=self.style.configure(".")["background"])

        home_frame = Frame(notebook, bg=LIGHT_GREY)
        mma_frame = Frame(notebook)
        nascar_frame = Frame(notebook)

        notebook.add(home_frame, text="Home")
        notebook.add(mma_frame, text="MMA")
        notebook.add(nascar_frame, text="Nascar")

        home_label = Label(home_frame, text="Home", bg=LIGHT_GREY).grid(row=0, column=0, padx=10, pady=10)
        mma_label = Label(mma_frame, text="MMA").grid(row=0, column=0, padx=10, pady=10)
        nascar_label = Label(nascar_frame, text="Nascar").grid(row=0, column=0, padx=10, pady=10)

        self.window.mainloop()
