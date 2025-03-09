import tkinter as tk
from tkinter import ttk
import datetime

from aux_functions import center_window

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        center_window(self, 620, 200)

        self.text = tk.Text(self, height=12)
        self.text.grid(column=0, row=0, sticky='NSEW', padx=5, pady=5)

        self.open_button = ttk.Button(
            self,
            text='Ask for my name',
            command=self.open_window
        )

        self.open_button.grid(column=0, row=1, padx=10, pady=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # We will set this value one the secondary window is closed
        self.my_name = None

    def open_window(self):
        self.secondary_window = SecondaryWindow(self)
        # grab_set will make the secondary window modal, so the user won't be able to interact with the main window
        self.secondary_window.grab_set()
        self.secondary_window.bind('<Destroy>', self.on_destroy_seconday_window)

    def on_destroy_seconday_window(self, event):
        # Check if the widget that triggered the event is the top level window
        # otherwise, the action would by executed one time for every window widget
        if event.widget == event.widget.winfo_toplevel():
            self.text.insert('1.0', f'{datetime.datetime.now()} -- Name: {self.my_name}\n')


class SecondaryWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        center_window(self, 300, 70)

        self.label = ttk.Label(self, text='Name: ')
        self.label.grid(column=0, row=0, padx=10, pady=10, sticky="W")
        self.entry = ttk.Entry(self)
        self.entry.grid(column=1, row=0, padx=10, pady=10, sticky="EW")

        self.button = ttk.Button(self, text='Save', command=self.submit)
        self.button.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

        self.grid_columnconfigure(1, weight=1)

    def submit(self):
        # Set the attribute my_name of the master window
        self.master.my_name = self.entry.get()
        # Close itself
        self.destroy()
        


app = MainWindow()
app.mainloop()