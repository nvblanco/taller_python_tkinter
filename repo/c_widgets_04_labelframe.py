import tkinter as tk
from tkinter import ttk

from aux_functions import center_window

root = tk.Tk()
center_window(root, 400, 200)

# Realign the label frame when a radio button is clicked
def on_radio_click():
    lf.pack_configure(side=alignment_var.get())
    


# Create a label frame
lf = ttk.LabelFrame(root, text='Alignment')
lf.pack(padx=20, pady=20, side="left")

alignment_var = tk.StringVar()
alignments = ('left', 'right')

grid_column = 0
for alignment in alignments:
    radio = ttk.Radiobutton(lf, text=alignment, value=alignment, variable=alignment_var, command=on_radio_click)
    radio.grid(column=grid_column, row=0, ipadx=10, ipady=10)
    grid_column += 1

root.mainloop()