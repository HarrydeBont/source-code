import tkinter as tk
from PIL import ImageTk, Image

#This creates the main window of an application
window = tk.Tk()
window.title("image_tkinter_exp")
window.geometry("800x300")
window.configure(background='grey')

path = "images/Harry de Bont.jpg"
#Open a New Image
image= Image.open(path)
width, height = image.size

# calculate ratio for desired resize
ratio = 100 / width
rwidth = int(ratio*width)
rheight = int(ratio*height)

#Resize Image using resize function
resized_image= image.resize((rwidth, rheight), Image.ANTIALIAS)
#Convert the image into PhotoImage
img = ImageTk.PhotoImage(resized_image)

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
#img = ImageTk.PhotoImage(Image.open(path))


#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)

# Show using grid geometry manager
panel.grid(row=0,column=0)



#Start the GUI
window.mainloop()



