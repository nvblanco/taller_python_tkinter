import tkinter as tk
from tkinter import ttk

from aux_functions import center_window

root = tk.Tk()
center_window(root, 250, 100)

# Set the weight of the first and second columns (2nd will be 3 times bigger)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# The parameter 'sticky' specifies which edge of the cell the widget should stick to
# It follows the cardinal directions: N, S, E, W, NE, NW, SE, SW
username_label = ttk.Label(root, text="Username:")
username_label.grid(column=0, row=0, sticky="W", padx=5, pady=5)
username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky="E", padx=5, pady=5)
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky="W", padx=5, pady=5)
password_entry = ttk.Entry(root,  show="*")
password_entry.grid(column=1, row=1, sticky="E", padx=5, pady=5)


login_button = ttk.Button(root, text="Login")
# The parameter 'columnspan' specifies how many columns the widget should span
# The parameter 'sticky=NSEW' stretches the widget to fill the cell horizontally and vertically
login_button.grid(column=0, row=2, columnspan=2, sticky="NSWE", padx=5, pady=5)
# To make the button expand to fill the cell, set the weight of the row to 1
root.rowconfigure(2, weight=1)

root.mainloop()