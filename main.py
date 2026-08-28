import tkinter as tk



def display_image(image1):
    label.config(image=image1)  # Update label text to indicate image capture
    label.image = image1        # Keep a reference to avoid garbage collection


def capture_image():
    # Placeholder function for capturing an image

    image1 = tk.PhotoImage(file="Test_Image1.png")
    display_image(image1)
    print("Capture Image button clicked!")
    # Here you would add the code to interface with the Raspberry Pi camera and capture an image

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

#####DISPLAY WINDOW#####
image = tk.PhotoImage(file="Test_Image.png")
label = tk.Label(root, image=image, width=600, height=500)
label.place(x=5, y=10)

#####ALL THE BUTTONS#####
button = tk.Button(root, text="Capture Image", width=25, command=capture_image)
button.place(x=610, y=10)

# 5. Start the event loop to keep the window open
root.mainloop()