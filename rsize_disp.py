# Module to be integrated in main_facR
# it resizes images for the userinterface
import cv2
from PIL import Image, ImageTk

# Classify
class Rsize:
    def __init__(self):
        pass

    def load_img(self, image_path, size):
        self.image_path = image_path
        #Open a New Image
        # CV2 portion
        self.image= cv2.imread(self.image_path) # CV2 image array
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        height, width = self.image.shape[:2]


        # calculate ratio for desired resize
        ratio = size / width
        rwidth = int(ratio*width)
        rheight = int(ratio*height)

        #Resize Image using resize function
        self.resized_image= cv2.resize(self.image, (rwidth, rheight), interpolation = cv2.INTER_AREA)

        # Convert the CV2 image into PhotoImage Tkinter
        img = self.resized_image
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        return(imgtk)
