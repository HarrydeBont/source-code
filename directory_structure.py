
# Bookkeeping of the directory structure
import os
import glob

class dir_struc:
    def __init__(self):
        self.main_root_dir = self.root_dir()
        image_path = "images"
        unknowns_path = "Unknown_faces"
        self.unknown_dir = os.path.join(self.main_root_dir, unknowns_path)
        self.image_dir = os.path.join(self.main_root_dir, image_path)
        
        self.image_dir = os.path.join(self.main_root_dir, image_path)

    def images_path(self):
        images_path = glob.glob(os.path.join(self.image_dir, "*.*"))
        return(images_path)

    def root_dir(self):
        main_root_directory = r"D:\Python"
        return(main_root_directory)

    def list_faces(self):
        """ 
        Returns the faces in the -images/- directory.
        """
        LSF = os.listdir(self.image_dir)

        return(LSF)

    def count_faces(self):
        """ 
        Returns the number of faces in the -images/- directory.
        """
        path = self.image_dir
        count = 0
        for x in os.listdir(path):
            if os.path.isfile(os.path.join(path,x)):
                count = count + 1
        return(count)

    def count_unknowns(self):
        """ 
        Returns the number of unknown faces in the -unknown/- directory.
        """
        path = self.unknown_dir
        count = 0
        for x in os.listdir(path):
            if os.path.isfile(os.path.join(path,x)):
                count = count + 1
        return(count)

