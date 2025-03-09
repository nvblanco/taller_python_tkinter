import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from aux_functions import center_window

root = tk.Tk()
center_window(root, 620, 200)

# Define the column names
columns = ('first_name', 'last_name', 'email')

# Create the TreeViewObject
# The parameter show='headings' hides the first empty column
tree = ttk.Treeview(root, columns=columns, show='headings')

# Define the text of the headings
tree.heading('first_name', text='First Name')
tree.heading('last_name', text='Last Name')
tree.heading('email', text='Email')

# Generate sample data
contacts = ((f'first {n}', f'last {n}', f'email{n}@example.com') for n in range(1, 100))

# Add data to the treeview
for contact in contacts:
    tree.insert('', "end", values=contact)


def item_selected(event):
    msg_lines = []
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        msg_lines.append(",".join(item['values']))
    showinfo(title='Information', message='\n'.join(msg_lines))

# Call the item_selected function when an item is selected
tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(row=0, column=0, sticky='NSEW')

# Add a scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='NS')

root.mainloop()