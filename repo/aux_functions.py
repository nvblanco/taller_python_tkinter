def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - width / 2)
    center_y = int(screen_height/2 - height / 2)
    root.geometry(f'{width}x{height}+{center_x}+{center_y}')