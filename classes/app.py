from tkinter import *
from tkinter import messagebox, ttk

MAIN_COLOR = "#ddd"
DARK_BLUE = "#2d3142"
LIGHT_GREY = "#bfc0c0"
WHITE = "#fff"
ORANGE = "#ef8354"
LIGHT_BLUE = "#4f5d75"
BLACK = "#000"

TAB_FONT = ("Lato", 10, "bold")
HEADER_FONT = ("Lato", 20, "bold")
CONTENT_FONT = ("Lato", 12, "bold")


class AppUI:

    def __init__(self):
        super().__init__()
        # Initial setup of tkinter, window title, etc
        self.window = Tk()
        self.window.title("DK Draft Studio")
        self.window.config(pady=10, padx=10, bg=DARK_BLUE)
        self.window.geometry("1024x768")
        self.window.resizable(True, True)

        # Create Notebook for Tabs
        notebook = ttk.Notebook(self.window)
        notebook.pack(fill=BOTH, expand=1)

        # Styling notebook
        self.style = ttk.Style()
        self.style.theme_create("DK_Style", parent="default", settings={
            "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0], "background": DARK_BLUE, "borderwidth": 0}},
            "TNotebook.Tab": {
                "configure": {"padding": [10, 4], "background": ORANGE, "foreground": BLACK,
                              "borderwidth": 0, "font": TAB_FONT}, }})
        self.style.theme_use("DK_Style")

        # Remove borders from notebook tabs
        self.style.layout("Tab",
                          [('Notebook.tab', {'sticky': 'nswe', 'children':
                              [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
                                  [('Notebook.label', {'side': 'top', 'sticky': ''})],
                                                     # })],
                                                     })],
                                             })]
                          )

        # Create menu bar
        self.menu = Menu(self.window)
        filemenu = Menu(self.menu, tearoff=0)
        filemenu.add_command(label="New")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.close_window)
        self.menu.add_cascade(label="File", menu=filemenu)
        helpmenu = Menu(self.menu, tearoff=0)
        helpmenu.add_command(label="Help Index")
        helpmenu.add_command(label="About")
        self.menu.add_cascade(label="Help", menu=helpmenu)
        self.window.config(menu=self.menu)

        # Create notebook frames
        home_frame = Frame(notebook, bg=LIGHT_BLUE)
        mma_frame = Frame(notebook, bg=LIGHT_BLUE)
        nascar_frame = Frame(notebook, bg=LIGHT_BLUE)

        # Add frames to notebook
        notebook.add(home_frame, text="Home")
        notebook.add(mma_frame, text="MMA")
        notebook.add(nascar_frame, text="Nascar")

        # Create labels for home frame
        home_label = Label(home_frame, text="Home", bg=LIGHT_BLUE, fg=LIGHT_GREY, font=HEADER_FONT)
        home_label.grid(row=0, column=0, padx=10, pady=10)

        # Create labels for mma frame
        mma_label = Label(mma_frame, text="MMA", bg=LIGHT_BLUE, fg=WHITE)
        mma_label.grid(row=0, column=0, padx=10, pady=10)

        # Create labels for nascar frame
        nascar_label = Label(nascar_frame, text="Nascar", bg=LIGHT_BLUE, fg=WHITE)
        nascar_label.grid(row=0, column=0, padx=10, pady=10)

        self.window.mainloop()

    def close_window(self):
        self.window.destroy()
        exit()
