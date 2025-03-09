import tkinter as tk

# Create the main window
root = tk.Tk()
# Set the title of the window
root.title("Basic window")

# Set the window size parameters
window_width = 600
window_height = 300

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# Set the geometry of the window (width x height + x + y)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Enable/disable window resizing (horizontal, vertical)
root.resizable(False, True)

# Set the window to be always on top
root.attributes('-topmost', 1)

# Start the main loop
root.mainloop()