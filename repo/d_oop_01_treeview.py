import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from aux_functions import center_window


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        center_window(self, 620, 200)

        self.tree = None
        self.scrollbar = None

        self.create_tree_widget()
        self.create_scrollbar()
        self.populate_tree()


    def create_tree_widget(self):
        columns = ('first_name', 'last_name', 'email')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        # define headings
        self.tree.heading('first_name', text='First Name')
        self.tree.heading('last_name', text='Last Name')
        self.tree.heading('email', text='Email')

        # Bind the delete key to the delete_item method
        self.tree.bind('<Delete>', self.delete_item)
        self.tree.grid(row=0, column=0, sticky=tk.NSEW)

    
    def create_scrollbar(self):
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

    def populate_tree(self):
        contacts = ((f'first {n}', f'last {n}', f'email{n}@example.com') for n in range(1, 100))

        for contact in contacts:
            self.tree.insert('', "end", values=contact)

    # Callback to delete the selected element
    def delete_item(self, event):
        for selected_item in self.tree.selection():
            self.tree.delete(selected_item)
        
app = App()
app.mainloop()