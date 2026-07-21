import tkinter as tk
# 1. Initialize the main application window
root = tk.Tk()

# 2. Set the title bar text
root.title("Raspberry Pi Camera Application")

# 3. Set the dimensions (Width x Height) in pixels
root.geometry("800x600")

# 4. (Optional) Set constraints for resizing
root.minsize(200, 150)

menu = tk.Menu(root)
root.config(menu=menu)

filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open...")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About")

# 5. Start the event loop to keep the window open
root.mainloop()