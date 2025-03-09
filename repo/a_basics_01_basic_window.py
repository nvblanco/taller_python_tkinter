import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the title of the window
root.title("Basic window")

# Set the geometry of the window (width x height + x + y)
# x and y are the position of the window top-left corner
root.geometry('600x400+100+100')

# Start the main loop
root.mainloop()