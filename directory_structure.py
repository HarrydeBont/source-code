# Bookkeeping of the directory structure
import os

class dir_struc:
    def __init__(self, terminalmessage = False):
        self.terminalmessage = terminalmessage
        image_path = "images"
        self.main_root_dir = self.root_dir()
        self.image_dir = os.path.join(self.main_root_dir, image_path)


    def root_dir(self):
        main_root_directory = "D://Python"
        return(main_root_directory)

    def list_faces(self, terminalmessage = False):
        """ 
        Returns the faces in the -images/- directory.
        """
        LSF = os.listdir(self.image_dir)
        if terminalmessage:
            print('-08052022-')
            print(type(LSF))
        return(LSF)

    def count_faces(self, terminalmessage = False):
        """ 
        Returns the number faces in the -images/- directory.
        """
        path = self.image_dir
        count = 0
        for x in os.listdir(path):
            if os.path.isfile(os.path.join(path,x)):
                count = count + 1
        if terminalmessage: print(count)
        return(count)

