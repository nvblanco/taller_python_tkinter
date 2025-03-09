import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from aux_functions import center_window

# Callback called when the button is clicked
def on_button_click():
    # Show a greeting message in a popup
    showinfo("Info" , f"Hi, {entry.get()}")

root = tk.Tk()
center_window(root, 400, 200)

# Put the text "Nome:" in the top of the window
label = ttk.Label(root, text="Nome:")
label.pack()

# Create an entry widget to get the user's name
entry = ttk.Entry(root)
entry.pack()

button = ttk.Button(root, text="Press me", command=on_button_click)
button.pack()

root.mainloop()