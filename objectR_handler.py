# This modue let's you store objects onto the physical drive
# Author: Harry de Bont,  2022
# reference: https://www.geeksforgeeks.org/create-a-directory-in-python/

import pickle
import os
objtr_root = "D://Python"

class objecter:
    """
    This class serializes objects, reads or saves them to file.
    Two functions: write_model (to file), read_model (from file)
    """
    def __init__(self, objtr_dir, objtr_file):
            self.objtr_dir:str = objtr_root + "//" + objtr_dir
            isDir = os.path.isdir(self.objtr_dir)
            self.objtr = self.objtr_dir + "//" + objtr_file + ".OBJTR"
            if isDir:
                print("object -"+ self.objtr_dir + " - path validated..")
            else:
                print(self.objtr_dir, " -object path doesn't exist. Create first to proceed.")
                ask_permission = input("Create directory [Y/N]: ?").upper()
                if ask_permission == "Y":
                    os.mkdir(self.objtr_dir)
                else:
                    print("Program exit, by user request.")
                    quit()


    def write_model(self, model_object, terminalmessage = False):
        with open(self.objtr, 'wb') as my_file: # write bytes to preserve the data
            pickle.dump(model_object, my_file)
            my_file.close()
            if terminalmessage: print("Object -" + self.objtr + "- saved.")

    def read_model(self, terminalmessage = False):
        with open(self.objtr, 'rb') as my_file:
            my_object = pickle.load(my_file)
            my_file.close()
            if terminalmessage: print("Retreiving -" + self.objtr + "- object.")
            return(my_object)