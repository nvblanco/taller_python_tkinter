import tkinter as tk
from tkinter import TclError, ttk


def create_input_frame(container):

    frame = ttk.Frame(container)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)

    # Find what
    ttk.Label(frame, text='Find what:').grid(column=0, row=0, sticky="W")
    keyword = ttk.Entry(frame, width=30)
    keyword.focus()
    keyword.grid(column=1, row=0, sticky="W")

    # Replace with:
    ttk.Label(frame, text='Replace with:').grid(column=0, row=1, sticky="W")
    replacement = ttk.Entry(frame, width=30)
    replacement.grid(column=1, row=1, sticky="W")

    # Match Case checkbox
    match_case = tk.StringVar()
    match_case_check = ttk.Checkbutton(
        frame,
        text='Match case',
        variable=match_case,
        command=lambda: print(match_case.get()))
    match_case_check.grid(column=0, row=2, sticky="W")

    # Wrap Around checkbox
    wrap_around = tk.StringVar()
    wrap_around_check = ttk.Checkbutton(
        frame,
        variable=wrap_around,
        text='Wrap around',
        command=lambda: print(wrap_around.get()))
    wrap_around_check.grid(column=0, row=3, sticky="W")

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=5)

    return frame


def create_button_frame(container):
    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight=1)

    ttk.Button(frame, text='Find Next').grid(column=0, row=0, padx=5, pady=5, sticky="EW")
    ttk.Button(frame, text='Replace').grid(column=0, row=1, padx=5, pady=5, sticky="EW")
    ttk.Button(frame, text='Replace All').grid(column=0, row=2, padx=5, pady=5, sticky="EW")
    ttk.Button(frame, text='Cancel').grid(column=0, row=3, padx=5, pady=5, sticky="EW")

    return frame



root = tk.Tk()
root.title('Replace')
root.resizable(False, False)

root.columnconfigure(0, weight=4)
root.columnconfigure(1, weight=1)

input_frame = create_input_frame(root)
input_frame.grid(column=0, row=0)

button_frame = create_button_frame(root)
button_frame.grid(column=1, row=0)

root.mainloop()
