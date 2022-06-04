# Save unknown faces to folder

import cv2
import os
from directory_structure import dir_struc
unknown_root = dir_struc()
from termess import terMess

My_msg = terMess()

class store_unknown:
    def __init__(self, unknown_dir, unknown_file):
        self.unknown_dir = unknown_dir
        
        self.unknown_counter = 0
        self.unknown_file:str = unknown_file + "-" + str(self.unknown_counter) +  ".jpg"
        self.unknown_counter_old = 0
        self.unknown_dir:str = unknown_root.root_dir() + "//" + self.unknown_dir
        isDir = os.path.isdir(self.unknown_dir)
        
        if isDir:
            msg = "object -"+ str(self.unknown_dir) + " - path validated.."
            print(msg)
        else:
            msg = str(self.unknown_dir) + " -file path doesn't exist. Create first to proceed."
            print(msg)
            ask_permission = input("Create directory [Y/N]: ?").upper()
            if ask_permission == "Y":
                os.mkdir(self.unknown_dir)
            else:
                My_msg.tprint("Program exit, by user request.")
                quit()
    
    def save_frame(self, frame):
        self.frame = frame
        self.unknown_file = self.unknown_file.replace(str(self.unknown_counter_old),str(self.unknown_counter))
        self.unknown_counter_old = self.unknown_counter
        self.unknown_counter += 1
        self.unknown_path = os.path.join(self.unknown_dir, self.unknown_file)
        cv2.imwrite(self.unknown_path,self.frame)