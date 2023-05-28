from tkinter import *
import by_mouse 
import by_cam
from PIL import Image, ImageTk
from random import randint

def open_mouse_window():
    # root_m = Tk()
    # root_m.title("Mouse Window")
    # Add your mouse window content here
   by_mouse.show_window()
   

def open_cam_window():
    # root_c = Tk()
    # root_c.title("Camera Window")
    # Add your camera window content here
    # root_c.mainloop()
    by_cam.show_window()

root = Tk()
root.title("Both")

mouse = Button(root, width=20, height=2, text="By Mouse", bg="#0ABDE3", fg="white", command=open_mouse_window)
mouse.grid(row=2, column=1)

cam = Button(root, width=20, height=2, text="By Camera", bg="#FF3E4D", fg="white", command=open_cam_window)
cam.grid(row=2, column=2)

root.mainloop()


