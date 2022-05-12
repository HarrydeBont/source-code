#Create a menu study
# following https://www.youtube.com/watch?v=AWPQXHR9vmA&ab_channel=Zenva
# interrupt a main loop
# https://www.youtube.com/watch?v=xDDjyVfwASc&ab_channel=TSInfoTechnologies
# Adding padding to a window
# Adding photo to grid geometry window -----> image_tkinter_exp
# Tkinter en OpenCV probleem: oplossing? https://stackoverflow.com/questions/32342935/using-opencv-with-tkinter 


from tkinter import Label, PhotoImage, ttk, Tk, StringVar, Entry, Button, Toplevel
import PIL.Image
import PIL.ImageTk
import tkinter as tk
from rsize_disp import Rsize
import testMainFunction
from directory_structure import dir_struc

class FaceApp:
    def __init__(self, root):
        root.title("Face recognition security and utilities.")
        root.iconbitmap('C:/Users/HWdeB/Documents/Python/source facerecogn/source code/faceR.ico')
        root.geometry("700x500")
        root.configure(bg = "grey")
        root.maxsize(2500, 1900)    

        # Start Face recognition program?
        Enter_button = Button(root, text="Start faceR", command=self.press_button_start)
        Enter_button.configure(font = ("Sansation", 12), fg = "black", bg = "#626563")
        Enter_button.grid(row=0,column=3)
             
        # List faces in window using custom libr.
        # Disp_portrait = Rsize()
        # self.img = Disp_portrait.load_img(self.path, 200)
        #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        #DispFace = Label(root, image = self.img)
        #DispFace.image = self.img # keep a reference! Tkinter bug fix >>> reference >>> https://web.archive.org/web/20201111190625id_/http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm
        #DispFace.grid(row=1,column=0)             
        Enter_button = Button(root, text="List trained faces", command=self.press_button_LSF)
        Enter_button.configure(font = ("Sansation", 12), fg = "black", bg = "#626563")
        Enter_button.grid(row=1,column=3)

        # Prompt user to enter a name
        label1 = Label(root, text="Enter the name of the person in this picture.")
        label1.configure(font = ("Sansation", 12), bg = "grey")
        label1.grid(row=2,column=0, ipadx=5,ipady=5)

        # Enter filename
        self.entry_text = StringVar()
        entry = Entry(root, textvariable = self.entry_text, borderwidth=2, relief='sunken')
        entry.configure(font = ("Sansation", 12), fg = "black")
        entry.grid(row=2, column=2, ipadx=1,ipady=1)
        
        # Enter assigning name?
        Enter_button = Button(root, text="Enter", command=self.press_button)
        Enter_button.configure(font = ("Sansation", 12), fg = "black", bg = "#626563")
        Enter_button.grid(row=2,column=3)

        # Confirmation text
        self.label_text = StringVar()
        label = Label(root, textvariable=self.label_text)
        label.configure(font = ("Sansation", 10), bg = "grey", fg = "black")
        label.grid()

        #  Reassignment done?
        done_button =  Button(root, text="Exit program?", command=lambda:root.destroy())
        done_button.configure(font = ("Sansation", 12), fg = "black", bg = "#626563")
        done_button.grid(row=5,column=3)
        
        # use directory environment
        self.use_dir = dir_struc()


    def press_button_LSF(self):
        text = "Listing faces."
        self.label_text.set(text)
        text = self.use_dir.list_faces()
        self.label_text.set(text)

    def press_button(self):
        text = "Assigning : '"+ self.entry_text.get() + "' to face recognition database."
        self.label_text.set(text)
        # print("Name assigned.")

    def press_button_start(self):
        text = "starting face recognition."
        testMainFunction.main()
        self.label_text.set(text)
        # print("Name assigned.")
root =  Tk()
FaceApp(root)
root.mainloop()

print("exit")
