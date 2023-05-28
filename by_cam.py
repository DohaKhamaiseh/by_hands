from tkinter import *

def show_window():
    root = Tk()
    root.title("Cam")

    msg = Label(root,font=50,bg="#9b59b6",fg="white",text="Hello from Camera")
    msg.grid(row=3,column=2)


    root.mainloop()