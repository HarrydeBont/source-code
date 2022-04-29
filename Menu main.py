#Create a menu study
# following https://www.youtube.com/watch?v=AWPQXHR9vmA&ab_channel=Zenva
# interrupt a main loop
# https://www.youtube.com/watch?v=xDDjyVfwASc&ab_channel=TSInfoTechnologies
# Adding padding to a window
# Adding photo to grid geometry window -----> image_tkinter_exp
# Tkinter bug fix

from tkinter import Label, PhotoImage, ttk, Tk, StringVar, Entry, Button, Toplevel
import PIL.Image
import PIL.ImageTk
import tkinter as tk
from rsize_disp import Rsize

class FaceApp:
    def __init__(self, root, path):
        self.path = path
        root.title("Face recognition security and utilities.")
        root.iconbitmap('C:/Users/HWdeB/Documents/Python/source facerecogn/source code/faceR.ico')
        root.geometry("700x300")
        root.configure(bg = "grey")
        root.maxsize(2500, 1900)

        # Show face in window using custom libr.
        Disp_portrait = Rsize()
        self.img = Disp_portrait.load_img(self.path)

        #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        DispFace = Label(root, image = self.img)
        DispFace.image = self.img # keep a reference! Tkinter bug fix >>> reference >>> https://web.archive.org/web/20201111190625id_/http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm
        DispFace.grid(row=0,column=0)
             
        
        # Prompt user to enter a name
        label1 = Label(root, text="Enter the name of the person in this picture.")
        label1.configure(font = ("Sansation", 12), bg = "grey")
        label1.grid(row=1,column=0, ipadx=5,ipady=5)

        # Enter filename
        self.entry_text = StringVar()
        entry = Entry(root, textvariable = self.entry_text, borderwidth=2, relief='sunken')
        entry.configure(font = ("Sansation", 12), fg = "black")
        entry.grid(row=1, column=2, ipadx=1,ipady=1)
        
        # Enter assigning name?
        Enter_button = Button(root, text="Enter", command=self.press_button)
        Enter_button.configure(font = ("Sansation", 12), fg = "black", bg = "#626563")
        Enter_button.grid(row=1,column=3)
        
        # Confirmation text
        self.label_text = StringVar()
        label = Label(root, textvariable=self.label_text)
        label.configure(font = ("Sansation", 10), bg = "grey", fg = "black")
        label.grid()

        #  Reassignment done?
        done_button =  Button(root, text="Exit program?", command=lambda:root.destroy())
        done_button.configure(font = ("Sansation", 12), fg = "black", bg = "#626563")
        done_button.grid(row=5,column=3)

    def press_button(self):
        text = "Assigning : '"+ self.entry_text.get() + "' to face recognition database."
        self.label_text.set(text)
        # print("Name assigned.")
root =  Tk()
FaceApp(root, "images/Robert Walraven.jpg")
root.mainloop()

print("exit")
