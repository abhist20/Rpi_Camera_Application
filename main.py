import tkinter as tk
import time
from time import sleep
from PIL import Image, ImageTk
from picamera2 import Picamera2, Preview

first = 0
picam2 = Picamera2()

def close_camera():
    global picam2
    print('Closing Camera...')
    picam2.close()  # Releases the hardware resource back to the OS
    
def display_image(image1):
    label.config(image=image1)  # Update label text to indicate image capture
    label.image = image1        # Keep a reference to avoid garbage collection

def capture_image():
    global first
    global picam2
    picam2.start()
    time.sleep(1)
    variable = (time.strftime("%y-%b-%d_%H:%M:%S"))
    picam2.capture_file('Test_Image1'+variable+'.png')
    picam2.stop()
    print("Capture Image button clicked!")
    # Here you would add the code to interface with the Raspberry Pi camera and capture an image

def start_camera():
    global picam2
    while 1:
        picam2.start()
        time.sleep(0.05)
        frame = picam2.capture_array()
        print(frame.shape)
        image1 = Image.fromarray(frame)
        image1 = ImageTk.PhotoImage(image1)
        display_image(image1)
        picam2.stop()
        root.update()
    
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
button = tk.Button(root, text="Start Camera", width=25, command=start_camera)
button.place(x=610, y=10)
button = tk.Button(root, text="Capture Image", width=25, command=capture_image)
button.place(x=610, y=50)
button = tk.Button(root, text="Stop Camera", width=25, command=close_camera)
button.place(x=610, y=100)
# 5. Start the event loop to keep the window open
root.mainloop()
print('Program exiting....Releasing all the harware.')
