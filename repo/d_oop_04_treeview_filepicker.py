import tkinter as tk
from tkinter import ttk

from aux_functions import center_window

class EmployeeManager(tk.Tk):
    def __init__(self):
        super().__init__()

        center_window(self, 620, 280)

        self.tree = None
        self.scrollbar = None

        self.create_tree_widget()
        self.create_scrollbar()
        self.populate_tree()
        self.create_buttons()

    def create_tree_widget(self):
        columns = ('first_name', 'last_name', 'email', 'department', 'position')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        # Set column width to the minimum
        for col in columns:
            self.tree.column(col, width=120, stretch=True)

        # define headings
        self.tree.heading('first_name', text='First Name')
        self.tree.heading('last_name', text='Last Name')
        self.tree.heading('email', text='Email')
        self.tree.heading('department', text='Department')
        self.tree.heading('position', text='Position')

        self.tree.grid(row=0, column=0, sticky=tk.NSEW)

    def create_scrollbar(self):
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

    def populate_tree(self):
        employees = ((f'first {n}', f'last {n}', f'email{n}@example.com') for n in range(1, 6))

        for emp in employees:
            self.tree.insert('', "end", values=emp)

    def create_buttons(self):
        self.add_button = ttk.Button(
            self,
            text='Add Employee',
            command=self.add_employee
        )
        self.add_button.grid(row=1, column=0, padx=10, pady=10)

        self.delete_button = ttk.Button(
            self,
            text='Delete Employee',
            command=self.delete_employee
        )
        self.delete_button.grid(row=2, column=0, padx=10, pady=10)

    def add_employee(self):
        self.dialog = AddEmployeeDialog(self)
        self.dialog.grab_set()

    def delete_employee(self):
        for selected_item in self.tree.selection():
            self.tree.delete(selected_item)


class AddEmployeeDialog(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        center_window(self, 300, 200)

        self.title('Add Employee')

        self.label = ttk.Label(self, text='First Name: ')
        self.label.grid(column=0, row=0, padx=10, pady=10, sticky="W")
        self.first_name = ttk.Entry(self)
        self.first_name.grid(column=1, row=0, padx=10, pady=10, sticky="EW")

        self.label = ttk.Label(self, text='Last Name: ')
        self.label.grid(column=0, row=1, padx=10, pady=10, sticky="W")
        self.last_name = ttk.Entry(self)
        self.last_name.grid(column=1, row=1, padx=10, pady=10, sticky="EW")

        self.label = ttk.Label(self, text='Email: ')
        self.label.grid(column=0, row=2, padx=10, pady=10, sticky="W")
        self.email = ttk.Entry(self)
        self.email.grid(column=1, row=2, padx=10, pady=10, sticky="EW")

        self.label = ttk.Label(self, text='Department: ')
        self.label.grid(column=0, row=3, padx=10, pady=10, sticky="W")
        self.department = ttk.Entry(self)
        self.department.grid(column=1, row=3, padx=10, pady=10, sticky="EW")

        self.label = ttk.Label(self, text='Position: ')
        self.label.grid(column=0, row=4, padx=10, pady=10, sticky="W")
        self.position = ttk.Entry(self)
        self.position.grid(column=1, row=4, padx=10, pady=10, sticky="EW")

        self.save_button = ttk.Button(self, text='Save', command=self.save)
        self.save_button.grid(column=0, row=5, padx=10, pady=10)

        self.cancel_button = ttk.Button(self, text='Cancel', command=self.cancel)
        self.cancel_button.grid(column=1, row=5, padx=10, pady=10)

        self.grid_columnconfigure(1, weight=1)

    def save(self):
        values = (
            self.first_name.get(),
            self.last_name.get(),
            self.email.get(),
            self.department.get(),
            self.position.get()
        )
        self.master.tree.insert('', "end", values=values)
        self.destroy()

    def cancel(self):
        self.destroy()


app = EmployeeManager()
app.title('Employee Manager')
app.mainloop()