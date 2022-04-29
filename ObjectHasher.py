# This Class is ment to hash objects and compare them
# (Re)witten by Harry de Bont
# April 2022

from objectR_handler import objecter
import os
import imagehash
from PIL import Image
from directory_structure import root_dir

main_root_dir = root_dir()
image_path = "images"
image_dir = os.path.join(main_root_dir, image_path)

class ObjectHash():
    def __init__(self, terminalmessage = False):
        self.terminalmessage = terminalmessage
        self.dir_model = 'directory hash'
        self.model_file = 'hash'
        self.prev_hash = objecter(self.dir_model, self.model_file)

    def CalcImageHash(self):
        """ 
        Returns the hashvalue of the images in -images/- directory.
        """
        count_files = 0
        current_hash = []
        if self.terminalmessage: print(os.listdir(image_dir))
        for filename in os.listdir(image_dir):
            current_hash.append(imagehash.average_hash(Image.open(image_dir+ "//" + filename)))
            if self.terminalmessage: print('Calculating hash, file nr. : ', count_files+1)
            count_files += 1

        # print('new ', current_hash)
        return(current_hash)

    def checkImage(self):
        """ 
        True :: Image hash is equal to previous hash, so need need to re-train the ML-model
        False :: Image hash is NOT equal to previous hash, you need to re-trainm the ML-model
        """
        hash_similar = True # True 
        # count_files = 0
        current_hash = []

        # Make a hash of all the file in image directory
        current_hash = self.CalcImageHash()    

        # open hash-file in hash-directory

        #check if directory with pictures has changed
        if self.prev_hash.read_model() == current_hash: #current calculated hash is equal to the previously stored hash?
            # print(prev_hash.read_model()) #debug
            # print("newly calculated: ", current_hash) #debug
            if self.terminalmessage: print("You allready trained the images: proceeding..")
            hash_similar = True
        else:
            if self.terminalmessage: print("You need to re-train your model, the previously trained model does not match all the provided faces")
            hash_similar = False
        return(hash_similar)