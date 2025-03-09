import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

from aux_functions import center_window

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        center_window(self, 620, 200)

        # Create a text editor of 12 lines
        self.text = tk.Text(self, height=12)
        self.text.grid(column=0, row=0, sticky='NSEW', padx=5, pady=5)

        # Button to open a file
        self.open_button = ttk.Button(
            self,
            text='Open a File',
            command=self.open_text_file
        )

        self.open_button.grid(column=0, row=1, padx=10, pady=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)


    def open_text_file(self):
        # Filetypes to show in the open file dialog
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )
        # Show the open file dialog
        f = fd.askopenfile(filetypes=filetypes)
        # Read the text file and show its content on the Text
        self.text.insert('1.0', f.readlines())


app = App()
app.mainloop()