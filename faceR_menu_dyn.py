# following: https://www.pythontutorial.net/tkinter/tkinter-thread/#:~:text=To%20create%20and%20control%20multiple,follow%20the%20Python%20threading%20tutorial.
# building Docker package
# https://stackoverflow.com/questions/1471994/what-is-setup-py
# How to install dlib library for Python in Windows 10
# https://medium.com/analytics-vidhya/how-to-install-dlib-library-for-python-in-windows-10-57348ba1117f
# build image error 
#        #8 22.76       ERROR: CMake must be installed to build dlib - Solved
# 18-06-2022: Create dynamic menu faceR_menu_dyn.py

from pickle import FALSE
import tkinter
import tkinter.messagebox
import customtkinter


import main_faceR
from objectR_handler import objecter
from messageBroker import mess_broker
from list_cv2_ports import list_ports
from directory_structure import dir_struc
import handle_ufaces

cu = dir_struc()
nu = cu.count_unknowns()
print('Number of unknowns faces :', nu)

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    WIDTH = 780
    HEIGHT = 520

    # ============ Creating a message broker to obtain messages ============ 

    def __init__(self):
        super().__init__()

        self.title("Face Recognition Security console")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        # self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ reading settings from config file ============
        self.faceR_config = objecter('config','FaceR_config') # creating configuration file object
        config_test = self.faceR_config.read_model(FALSE)
        self.show_m = config_test[1]
        self.initdone = 0


        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(6, weight=30)  # empty row as spacing
        # self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        # self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="FaceR menu",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        
        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Start FaceR",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.start_faceR_event)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Unknown Faces",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.uf_button_event)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.switch_1 = customtkinter.CTkSwitch(master=self.frame_left,
                                                text="Registry On/Off")
        self.switch_1.grid(row=9, column=0, pady=10, padx=20, sticky="w")

        self.switch_2 = customtkinter.CTkSwitch(master=self.frame_left,
                                                text="Dark Mode",
                                                command=self.change_mode)
        self.switch_2.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

    def uf_button_event(self):
        print("Handling Unknown faces")
        self.uf_button_3 = customtkinter.CTkButton(master=self.frame_right,
                                                height=25,
                                                text="<< Prev",
                                                command= self.uf_prev)
        self.uf_button_3.grid(row=2, column=1, columnspan=1, pady=10, padx=5, sticky="w")
        self.uf_button_2 = customtkinter.CTkButton(master=self.frame_right,
                                                height=25,
                                                text="Next >>",
                                                command=self.uf_next)
        self.uf_button_2.grid(row=2, column=3, columnspan=1, pady=10, padx=5, sticky="e")
        self.uf_button_4 = customtkinter.CTkButton(master=self.frame_right,
                                                height=25,
                                                text="Done",
                                                command=self.remove_nav_menu)
        self.uf_button_4.grid(row=3, column=2, columnspan=1, pady=10, padx=5, sticky="e")

        #handle_ufaces.show()
    
    def remove_nav_menu(self):
        self.uf_button_2.grid_forget()
        self.uf_button_3.grid_forget()
        self.uf_button_4.grid_forget()

    def uf_next(self):
        print("Next")
        handle_ufaces.next()
    
    def uf_prev(self):
        print("Prev")
        handle_ufaces.prev()

    def start_faceR_event(self):
        print("Start Face Recognition")
        main_faceR.faceR(1)
             

    def change_mode(self):
        if self.switch_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        # ==== Executed once before start-up ====
        #self.t2.start()
        self.mainloop()

if __name__ == "__main__":
    app = App()
    app.start()
    # ====== execute after Main loop execution has ended ===================