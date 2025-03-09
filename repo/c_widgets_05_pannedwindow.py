import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('PanedWindow Demo')
root.geometry('300x200')

# Create a PanedWindow with orziontal orientation (from left to right)
pw = ttk.PanedWindow(orient=tk.HORIZONTAL)

# Left listbox
langs = ('Java', 'C#', 'C', 'C++', 'Python',
         'Go', 'JavaScript', 'PHP', 'Swift')
var_lang = tk.Variable(value=langs)
left_list = tk.Listbox(
    root,
    listvariable=var_lang,
    selectmode=tk.EXTENDED)
left_list.pack(side=tk.LEFT)
pw.add(left_list)

# Right listbox
fruits = ('Melon', 'Apple', 'Orange', 'Banana', 
          'Citrus', 'Plum', 'Mandarin')
var_fruit = tk.Variable(value=fruits)
right_list = tk.Listbox(
    root,
    listvariable=var_fruit,
    selectmode=tk.EXTENDED)
right_list.pack(side=tk.LEFT)
pw.add(right_list)

# place the panedwindow on the root window
pw.pack(fill=tk.BOTH, expand=True)

root.mainloop()