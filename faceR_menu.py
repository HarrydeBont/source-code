from pickle import FALSE
import tkinter
import tkinter.messagebox
from click import command

from matplotlib.pyplot import show, text
import threading
import customtkinter
import main_faceR
from objectR_handler import objecter
from messageBroker import mess_broker

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    
    WIDTH = 780
    HEIGHT = 520
    global y    # for demonstration purpose only
    y = 0

    # ============ Creating a message brokerto obtain messages ============
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
                                                command=threading.Thread(target=self.start_faceR_event).start())
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
        self.slider_button_1.configure(state=tkinter.DISABLED, text="Read more")
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
        config_test = self.faceR_config.read_model()
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
        main_faceR.faceR()

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
        
        self.mainloop()
    
   


if __name__ == "__main__":
    app = App()
    app.start()
    # ====== execute after Main loop execution has ended ===================
    
