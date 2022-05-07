from tkinter import *
import cv2
import os
from PIL import ImageTk, Image
from rsize_disp import Rsize

set_size = 200

def nex_img(i):   # takes the current scale position as an argument
    # delete previous image
    canvas.delete('image')
    # create next image
    canvas.create_image(20, 20, anchor=NW, image=listimg[int(i)-1], tags='image')

root = Tk()

image1 = Rsize()
image2 = Rsize()
image3 = Rsize()
image1 = image1.load_img('D:/Python/images/Harry de Bont.jpg', set_size)

image2 = image2.load_img('D:/Python/images/Fabian de Bont.jpg', set_size)
img_height, img_width = image2.shape[:2]
image3 = image3.load_img('D:/Python/images/Katelijn de Bont.jpg', set_size)

listimg = [image1, image2, image3]

scale = Scale(master=root, orient=HORIZONTAL, from_=1, to=len(listimg), resolution=1,
              showvalue=False, command=nex_img)
scale.pack(side=BOTTOM, fill=X)
canvas = Canvas(root, width=img_width+50, height=img_height+10)
canvas.pack()

# show first image
nex_img(1)

root.mainloop()