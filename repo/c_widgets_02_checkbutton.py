import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

from aux_functions import center_window

root = tk.Tk()
center_window(root, 400, 300)

selected_size = tk.StringVar()
agreement = tk.StringVar()

def show_selected_size():
    if agreement.get() != 'agree':
        showerror( # Show an error message box
            title='Result',
            message='You must agree to the terms first'
        )
        return
    
    else:
        showinfo(
            title='Result',
            message=selected_size.get()
        )

label = ttk.Label(text="What's your t-shirt size?")
label.pack(fill="x", padx=5, pady=5)

sizes = (('Small', 'S'),
         ('Medium', 'M'),
         ('Large', 'L'),
         ('Extra Large', 'XL'),
         ('Extra Extra Large', 'XXL'))

for size_text, size_symbol in sizes:
    r = ttk.Radiobutton(
        root,
        text=size_text,
        value=size_symbol,
        variable=selected_size
    )
    r.pack(fill="x", padx=5, pady=5)

# Draw a horizontal line to separate two window sections
sep = ttk.Separator(root,orient='horizontal')
sep.pack(fill="x", padx=5, pady=20)


check_button = ttk.Checkbutton(root,
                text='I agree',
                variable=agreement,
                onvalue='agree',
                offvalue='disagree')
check_button.pack(padx=5, pady=10)

# button
button = ttk.Button(
    root,
    text="Get Selected Size",
    command=show_selected_size)
button.pack(fill="x", padx=5, pady=5)

root.mainloop()