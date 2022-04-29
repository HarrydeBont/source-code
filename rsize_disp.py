# Module to be integrated in main_facR
# it resizes images for the userinterface
# import tkinter as tk
from PIL import ImageTk, Image

# Classify
class Rsize:
    def __init__(self):
        print("doing nothing for now..")
        pass

    def load_img(self, image_path):
        self.image_path = image_path
        #Open a New Image
        self.image= Image.open(self.image_path)
        width, height = self.image.size

        # calculate ratio for desired resize
        ratio = 100 / width
        rwidth = int(ratio*width)
        rheight = int(ratio*height)

        #Resize Image using resize function
        self.resized_image= self.image.resize((rwidth, rheight), Image.ANTIALIAS)

        # Convert the image into PhotoImage
        img = ImageTk.PhotoImage(self.resized_image)
        return(img)
