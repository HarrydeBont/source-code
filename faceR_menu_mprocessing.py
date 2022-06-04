# following: https://www.pythontutorial.net/tkinter/tkinter-thread/#:~:text=To%20create%20and%20control%20multiple,follow%20the%20Python%20threading%20tutorial.
# building Docker package
# https://stackoverflow.com/questions/1471994/what-is-setup-py
# How to install dlib library for Python in Windows 10
# https://medium.com/analytics-vidhya/how-to-install-dlib-library-for-python-in-windows-10-57348ba1117f
# build image error 
        # Building wheel for dlib (setup.py): finished with status 'error'
        #8 22.76   error: subprocess-exited-with-error
        #8 22.76   
        #8 22.76   × python setup.py bdist_wheel did not run successfully.
        #8 22.76   │ exit code: 1
        #8 22.76   ╰─> [10 lines of output]
        #8 22.76       running bdist_wheel
        #8 22.76       running build
        #8 22.76       running build_py
        #8 22.76       package init file 'tools/python/dlib/__init__.py' not found (or not a regular file)
        #8 22.76       warning: build_py: byte-compiling is disabled, skipping.
        #8 22.76       
        #8 22.76       running build_ext
        #8 22.76       
        #8 22.76       ERROR: CMake must be installed to build dlib
        #8 22.76       
        #8 22.76       [end of output]
        #8 22.76   
        #8 22.76   note: This error originates from a subprocess, and is likely not a problem with pip.
        #8 22.76   ERROR: Failed building wheel for dlib
        #8 22.76   Running setup.py clean for dlib
        #8 23.37   Building wheel for face-recognition-models (setup.py): started
        #8 35.77   Building wheel for face-recognition-models (setup.py): finished with status 'done'
        #8 35.99   Created wheel for face-recognition-models: filename=face_recognition_models-0.3.0-py2.py3-none-any.whl size=100566186 sha256=b6e2f5d8288476ed5e4fb89f864677a0681d755310cb18c8d052944646c95d52
        #8 35.99   Stored in directory: /root/.cache/pip/wheels/b4/4b/8f/751e99d45f089bdf366a7d3e5066db3c2b84a62e4377f534d7
        #8 35.99   Building wheel for ImageHash (setup.py): started
        #8 36.68   Building wheel for ImageHash (setup.py): finished with status 'done'
        #8 36.68   Created wheel for ImageHash: filename=ImageHash-4.2.1-py2.py3-none-any.whl size=295206 sha256=55878d5adc454b90d41f1a415bda1ef0b41066cd999501ba283dd70cd1237423
        #8 36.68   Stored in directory: /root/.cache/pip/wheels/48/a1/7f/096c1269d6bf78d4768180602579b35a1e8cb1250bb4b40c74
        #8 36.69 Successfully built face-recognition-models ImageHash
        #8 36.69 Failed to build dlib
        #8 36.90 Installing collected packages: face-recognition-models, dlib, cmake, six, pyparsing, Pillow, numpy, kiwisolver, fonttools, cycler, colorama, click, scipy, PyWavelets, python-dateutil, packaging, opencv-python, face-recognition, matplotlib, ImageHash
        #8 37.75   Running setup.py install for dlib: started
        #8 38.44   Running setup.py install for dlib: finished with status 'error'
        #8 38.44   error: subprocess-exited-with-error
        #8 38.44   
        #8 38.44   × Running setup.py install for dlib did not run successfully.
        #8 38.44   │ exit code: 1
        #8 38.44   ╰─> [10 lines of output]
        #8 38.44       running install
        #8 38.44       running build
        #8 38.44       running build_py
        #8 38.44       package init file 'tools/python/dlib/__init__.py' not found (or not a regular file)
        #8 38.44       warning: build_py: byte-compiling is disabled, skipping.
        #8 38.44       
        #8 38.44       running build_ext
        #8 38.44       
        #8 38.44       ERROR: CMake must be installed to build dlib
        #8 38.44       
        #8 38.44       [end of output]
        #8 38.44   
        #8 38.44   note: This error originates from a subprocess, and is likely not a problem with pip.
        #8 38.44 error: legacy-install-failure
        #8 38.44 
        #8 38.44 × Encountered error while trying to install package.
        #8 38.44 ╰─> dlib
# Try follow https://packaging.python.org/en/latest/guides/packaging-namespace-packages/#native-namespace-packages

from ast import arg
from pickle import FALSE
import tkinter
import tkinter.messagebox
import multiprocessing
import concurrent.futures
from matplotlib.pyplot import show, text
import time

import customtkinter


import main_faceR
from objectR_handler import objecter
from messageBroker import mess_broker
from list_cv2_ports import list_ports
from directory_structure import dir_struc

cu = dir_struc()
nu = cu.count_unknowns()
print('Number of unknowns faces :', nu)

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

# ============ Acquiring available cameras ============
# creating list of camera ports
# global AC
# AC = list_ports()


class App(customtkinter.CTk):
    
    WIDTH = 780
    HEIGHT = 520
    global y    # for demonstration purpose only
    y = 0

    # ============ Creating a message broker to obtain messages ============
    global UImess
    UImess = mess_broker()
    

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
        
        # ============ Initializing multiprocessing ============
        # creating processes
        
        self.p1 = multiprocessing.Process(target=main_faceR.faceR, args= (3,))
        self.p2 = multiprocessing.Process(target=main_faceR.faceR, args= (0,))
        self.p3 = multiprocessing.Process(target=main_faceR.faceR, args =(1,))



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
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

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
                                                command=self.button_event)
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Display registry",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.button_event)
        self.button_3.grid(row=4, column=0, pady=10, padx=20)

        self.button_4 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Terminal messages",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                command=self.read_messages)
        self.button_4.grid(row=5, column=0, pady=10, padx=20)

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



        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="FaceR display messageBroker messages here,\n" +
                                                        "messages need to have destination \n" +
                                                        "'ui' on in order to show here." ,
                                                   height=100,
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

        self.progressbar = customtkinter.CTkProgressBar(master=self.frame_info)
        self.progressbar.grid(row=1, column=0, sticky="ew", padx=15, pady=15)

        # ============ frame_right ============

        self.radio_var = tkinter.IntVar(value=0)

        self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
                                                        text="FaceR options:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, pady=20, padx=10, sticky="")

        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        # self.slider_1 = customtkinter.CTkSlider(master=self.frame_right,
        #                                         from_=0,
        #                                         to=1,
        #                                         number_of_steps=3,
        #                                         command=self.progressbar.set)
        
        #self.slider_1.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        self.slider_2 = customtkinter.CTkSlider(master=self.frame_right,
                                                command=self.progressbar.set)
        self.slider_2.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        self.slider_button_1 = customtkinter.CTkButton(master=self.frame_right,
                                                       height=25,
                                                       text="Security interval",
                                                       command=self.button_event)
        self.slider_button_1.grid(row=4, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.slider_button_2 = customtkinter.CTkButton(master=self.frame_right,
                                                       height=25,
                                                       text="CTkButton2",
                                                       command=self.button_event)
        self.slider_button_2.grid(row=5, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.checkbox_button_1 = customtkinter.CTkButton(master=self.frame_right,
                                                         height=25,
                                                         text="CTkButton",
                                                         border_width=3,   # <- custom border_width
                                                         fg_color=None,   # <- no fg_color
                                                         command=self.button_event)
        self.checkbox_button_1.grid(row=6, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.check_box_1 = customtkinter.CTkCheckBox(master=self.frame_right,
                                                     text="CTkCheckBox1")
        self.check_box_1.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        self.termess_box = customtkinter.CTkCheckBox(master=self.frame_right,
                                                     text="Terminal messages",command=self.termess_event) # All initialization arguments for tkinter widgets are keyword only, except
        self.termess_box.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Name unknown face")
        self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Enter name",
                                                command=self.button_event)
        self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        # set default values
        self.radio_button_1.select()
        self.switch_2.select()
        #self.slider_1.set(0.2)
        if UImess.ql('ui') > 0:
            ql = 1
        else:
            ql = 0
        self.slider_2.set(ql)
        self.progressbar.set(0.5)
        self.slider_button_1.configure(state=tkinter.DISABLED)
        self.radio_button_3.configure(state=tkinter.DISABLED) # state=tkinter.DISABLED, text="CheckBox disabled"
        self.check_box_1.configure()
        if self.show_m:
            self.termess_box.select()
        else: 
            self.termess_box.deselect()

    def termess_event(self):
        # writing config file
        # config_test = []
        # config_test.append('show_m')
        # show_m = 1 # 1 :: show messages 
        # config_test.append(show_m)

        # faceR_config.write_model(config_test, True)

        # Reading config file to check if terminal messages should be on
        config_test = self.faceR_config.read_model(False)
        self.show_m = config_test[1]
        if self.initdone:  # this event is called a a first time upon intialization (I don't know why) initdone is to prevent unwanted action when intialization
            if self.show_m: 
                self.show_m = 0
            else: 
                self.show_m = 1
            config_test[1] = self.show_m
        else: self.initdone = 1
        
        if self.show_m ==1: 
            state= 'ON ---'
            msg = str(config_test[0]) + str(config_test[1]) + '--- Terminal messages '+ state
            print(msg)
        else: 
            state = 'OFF ---'
        
        config_test[1] = self.show_m
        self.faceR_config.write_model(config_test, self.show_m)

    def button_event(self):
        global y
        y += 1
        x = str(y)
        self.label_info_1.config(text=x)
        print("Button pressed")

    def start_faceR_event(self):
        print("Start Face Recognition")
        #self.button_1.configure(state=tkinter.DISABLED, text="---")
        # try:
        #     self.p1.start()
        # except:
        #     print('something went wrong.. process p1')
        # time.sleep(0.2)
        # try:
        #     self.p2.start()
        # except:
        #     print('something went wrong.. process p2')
        # time.sleep(5)
        # try:
        #     self.p3.start()
        # except:
        #     print('something went wrong.. process p3')
        with concurrent.futures.ProcessPoolExecutor() as executor:
            main_faceR.faceR(1)
            main_faceR.faceR(3)
        #main_faceR.faceR()
       

    def read_messages(self):
        pullmsg = UImess.getmsg('ui')
        if pullmsg != None:
            x = pullmsg
            self.label_info_1.config(text=x)
        else:
            self.label_info_1.config(text = 'End of message queue..')

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
    
