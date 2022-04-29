import tkinter as tk
from tkinter import Label, PhotoImage, ttk, Tk, StringVar, Entry, Button, Toplevel
# this into Menu main
from rsize_disp import Rsize

from PIL import ImageTk, Image

#This creates the main window of an application
window = Tk()
window.title("image_tkinter_exp")
window = Toplevel()
window.iconbitmap('C:/Users/HWdeB/Documents/Python/source facerecogn/source code/faceR.ico')
window.geometry("1900x1400")
window.maxsize(2500, 1900)
path = "images/Harry de Bont.jpg"

# this into Menu main
Disp_portrait = Rsize()
img = Disp_portrait.load_img(path)


#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)

# Show using grid geometry manager
panel.grid(row=0,column=0)



#Start the GUI
window.mainloop()