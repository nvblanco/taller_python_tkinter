import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from aux_functions import center_window

root = tk.Tk()

# Create a Tkinter variable that will store a list of programming languages
langs = ('Java', 'C#', 'C', 'C++', 'Python',
         'Go', 'JavaScript', 'PHP', 'Swift')
var = tk.Variable(value=langs)

# Create a listbox widget and assign the variable to it
listbox = tk.Listbox(
    root,
    listvariable=var,
    height=6, # Number of visible items
    selectmode=tk.EXTENDED) # Allows multiple selection

listbox.pack(expand=True, # When the window is resized, the listbox will expand
             fill="both", # Fill the entire window
             side="left") # Align to the left

# Link a scrollbar to a list
scrollbar = ttk.Scrollbar(
    root,
    orient=tk.VERTICAL, # Vertical orientation
    command=listbox.yview # Link the scrollbar to the vertical view of the listbox
)

listbox['yscrollcommand'] = scrollbar.set

scrollbar.pack(side=tk.LEFT, expand=True, fill="y")


def items_selected(event):
    # Get a tuple with the selected indices (starts at 0)
    selected_indices = listbox.curselection()
    selected_langs = ",".join([listbox.get(i) for i in selected_indices])

    showinfo(title='Information', message=f"You selected: {selected_langs}")

# Bind the event of selecting an item to the function items_selected
listbox.bind('<<ListboxSelect>>', items_selected)

root.mainloop()