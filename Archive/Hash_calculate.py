import os
from PIL import Image
import imagehash
hash_dir = 'directory hash'
hash_file = 'hash'

def CalcImageHash(terminalmesssage = False):
    """ 
    Returns the hashvalue of the images in -images/- directory.
    """
    count_files = 0
    current_hash = []
    if terminalmesssage: print(os.listdir('images//'))
    for filename in os.listdir('images//'):
        current_hash.append(imagehash.average_hash(Image.open('images//' + filename)))
        if terminalmesssage: print('Calculating hash, file nr. : ', count_files+1)
        count_files += 1

    # print('new ', current_hash)
    return(current_hash)