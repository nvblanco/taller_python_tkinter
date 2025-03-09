import tkinter as tk
from tkinter import ttk # Themed Tkinter (if not available use tk instead)

from aux_functions import center_window

# Callbacks called when the button is clicked
def on_button_click_command():
    button["text"] = "Button clicked (via command)"

def on_button_click_bind(event):
    print("Button clicked (via bind)")
    print(f"\tEvent: {event}")

root = tk.Tk()
# Use an auxiliary function to center the window on the screen
center_window(root, width=400, height=200)

# Create a button with the text "Press me" and the callback on_button_click
# Note that the first parameter when creating a tkinter widget is the parent widget
# In this case, the parent widget is the main window
button = ttk.Button(root, text="Press me", command=on_button_click_command)
# Oher ways to configure the button (if created without parameters)
# label.config(text="Press me")
# label["text"] = "Press me"

# Bind the button to the on_button_click_bind callback when the left mouse button is clicked
button.bind("<Button-1>", on_button_click_bind)

# Pack the themed button into the window
button.pack()

root.mainloop()