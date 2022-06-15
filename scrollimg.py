from tkinter import *
import os
from PIL import ImageTk, Image

def nex_img(i):   # takes the current scale position as an argument
    # delete previous image
    canvas.delete('image')
    # create next image
    canvas.create_image(20, 20, anchor=NW, image=listimg[int(i)-1], tags='image')
# "D:\Python\Unknown_faces\rename me please-15.jpg"
root = Tk()
image1 = ImageTk.PhotoImage(Image.open(r'D:\\Python\\Unknown_faces\\rename me please-0.jpg'))
image2 = ImageTk.PhotoImage(Image.open(r'D:\\Python\\Unknown_faces\\rename me please-1.jpg'))
image3 = ImageTk.PhotoImage(Image.open(r'D:\\Python\\Unknown_faces\\rename me please-2.jpg'))
listimg = [image1, image2, image3]

scale = Scale(master=root, orient=HORIZONTAL, from_=1, to=len(listimg), resolution=1,
              showvalue=False, command=nex_img)
scale.pack(side=BOTTOM, fill=X)
canvas = Canvas(root, width=800, height=600)
canvas.pack()

# show first image
nex_img(1)

root.mainloop()