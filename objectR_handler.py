# This modue let's you store objects onto the physical drive
# Author: Harry de Bont,  2022
# reference: https://www.geeksforgeeks.org/create-a-directory-in-python/

import pickle
import os
from directory_structure import dir_struc

objtr_root = dir_struc()

class objecter:
    """
    This class serializes objects, reads or saves them to file.
    Two functions: write_model (to file), read_model (from file)
    """
    def __init__(self, objtr_dir, objtr_file, terminalmessage = True):
            self.objtr_dir:str = objtr_root.root_dir() + '\\' + objtr_dir
            isDir = os.path.isdir(self.objtr_dir)
            self.objtr = self.objtr_dir + "\\" + objtr_file + ".OBJTR"
            if isDir:
                msg = "object -"+ self.objtr_dir + " - directory validated.."
                if terminalmessage: print(msg)
            else:
                msg = self.objtr_dir, " -object path doesn't exist. Create first to proceed."
                if terminalmessage: print(msg)
                ask_permission = input("Create directory [Y/N]: ?").upper()
                if ask_permission == "Y":
                    os.mkdir(self.objtr_dir)
                else:
                    if terminalmessage: print("Program exit, by user request.")
                    quit()


    def write_model(self, model_object, terminalmessage = False):
        with open(self.objtr, 'wb') as my_file: # write bytes to preserve the data
            pickle.dump(model_object, my_file)
            my_file.close()
            msg = "Object -" + self.objtr + "- saved."
            if terminalmessage: print(msg)

    def read_model(self, terminalmessage = False):
        # Check whether the 
        # specified path - self.objtr - is 
        # an existing file.
        isFile = os.path.isfile(self.objtr)
        if isFile:
            with open(self.objtr, 'rb') as my_file:
                my_object = pickle.load(my_file)
                my_file.close()
                msg = "Retreiving -" + self.objtr + "- object."
                if terminalmessage: print(msg)
                return(my_object)
        else:
            msg = 'Program exit file', str(self.objtr), ' does not exist.'
            if terminalmessage: print(msg)
            quit()
    
    def verify_file(self):
        isFile = os.path.isfile(self.objtr)
        return(isFile)