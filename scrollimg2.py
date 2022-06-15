import cv2
import glob
import os
from FaceR.directory_structure import dir_struc
import directory_structure


ud = dir_struc()
path = glob.glob(os.path.join(ud.unknown_path(), ud.unknown_type()))

for file in path:
    img = cv2.imread(file)
    cv2.imshow(str(file), img)
    cv2.waitKey()
    cv2.destroyAllWindows()

