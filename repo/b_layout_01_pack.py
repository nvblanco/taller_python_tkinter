import tkinter as tk
from tkinter import ttk

from aux_functions import center_window

root = tk.Tk()
center_window(root, 400, 200)

label1 = tk.Label(master=root, text='Tkinter',bg='red',fg='white')
label2 = tk.Label(master=root,text='Pack Layout',bg='green', fg='white')
label3 = tk.Label(master=root, text='Demo',bg='blue', fg='white', font=('Helvetica',14))

# Parameter 'side' can be 'top' (top to bottom), 'bottom' (bottom to top), 
# 'left' (left to right), or 'right' (right to left). If not specified,
# the default value is 'top'

# The parameter 'expand' determines whether the widget should expand to occupy
# all the available space in the parent widget. If not specified, the default
# value is False

# The parameter 'fill' determines if a widget will occupy the availabe space. It
# accepts values 'x', 'y', 'both', and 'none'. If not specified, the default 
# value is 'none'

# Parameters 'ipadx' and 'ipady' determine the internal padding of the widget

# Parameters 'padx' and 'pady' determine the external padding of the widget

label1.pack(side="top", expand=True)
label2.pack(side="top", expand=True, fill="y", ipadx=20, ipady=20)
label3.pack(side="top", fill="x", pady=10)

root.mainloop()