# This module checks whether the content of a directory with images has changed compared to the last time it checked.
# https://prabhugs.wordpress.com/2011/08/27/143/  pickle as a way to read and write a hash to a file
# https://pypi.org/project/ImageHash/ 
# Issues I was confused by the  average hash function, it doesn't averages out the hash of all the images, to be continued // Solved by creating an objerct that is a list of hashed images from the images-directory
# Next to do = incorporate in main_faceR... (Done)

import pickle
import os
from PIL import Image
import imagehash
from objectR_handler import objecter
from Archive.Hash_calculate import CalcImageHash

dir_model = 'directory hash'
model_file = 'hash'
prev_hash = objecter(dir_model, model_file)

def checkImage(terminalmessage = False):
    """ 
    True :: Image hash is equal to previous hash, so need need to re-train the ML-model
    False :: Image hash is NOT equal to previous hash, you need to re-trainm the ML-model
    """
    hash_similar = True # True 
    # count_files = 0
    current_hash = []

    # Make a hash of all the file in image directory
    current_hash = CalcImageHash()    

    # open hash-file in hash-directory

    #check if directory with pictures has changed
    if prev_hash.read_model() == current_hash: #current calculated hash is equal to the previously stored hash?
        # print(prev_hash.read_model()) #debug
        # print("newly calculated: ", current_hash) #debug
        if terminalmessage: print("You allready trained the images: proceeding..")
        hash_similar = True
    else:
        if terminalmessage: print("You need to re-train your model, the previously trained model does not match all the provided faces")
        hash_similar = False
    return(hash_similar)