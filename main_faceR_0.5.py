# This program is an attempt to program a FACE RECOGNITION ready for home automation
# Author: Harry de Bont 2022
# Version history / To do next: 
# 1) Re-load previously trained model when no pictures have been added. done V 15-4-2022 (Objjecthasher)
# 2) Hashing_images and Hash_calculate in one Class done V 19-04-2022 (ObjectHasher)
# 3) Make a Register library-routine  done V 25-04-2022 (F_rec_register)
# 4) Save images of non-recognized faces done V 29-04-2022 (Unknown_faces)
# 5) Use saved image as training input done V 29-04-2022 (works without changes)
# 6) Create multiple photo-entries for one person done V 29-04-2022 (undoubling)
# 7) Move face images to root directory as well (D:/Python) done V 29-04-2022 (directory_structure)
# 8) Use the stored face-registration after re-start. done V 09-05-2022 (F_rec_register)
# 9) Create terminal message routine to be used in all modules. Terminal messages can be shown either in UI or in the terminal window.
#       Done: main_face_0.5, termess, objectR_handler, ObjectHasher, simple_facerecF_rec_register, directory_structure, unknown_faces, undoubling, removed unnecessary terminalmessage var 
# 10) Create objecter configuration file. done V 12-05-2022 (temp code in main_face_05)
# 9) Create user interace. busy (re-use Custom Tkinter master and create main_faceR)
# 10) Make a routine for copying unknown faced to images (supervised so need to use UI)
# 11) Make executable

from tkinter import image_types
import cv2
from objectR_handler import objecter
from simple_facerec import SimpleFacerec
from F_rec_register import register_faceR
from unknown_faces import store_unknown
from termess import terMess
from undoubling import undouble
from directory_structure import dir_struc

My_msg = terMess()
faceR_config = objecter('config','FaceR_config')

# writing config file
# config_test = []
# config_test.append('show_m')
# show_m = 1 # 1 :: show messages 
# config_test.append(show_m)

# faceR_config.write_model(config_test, True)

# Reading config file
# config_test = faceR_config.read_model()
# show_m = config_test[1]

main_root_dir = dir_struc()
#image_path = "images"
msg = str(main_root_dir.list_faces())
image_path = main_root_dir.images_path()
My_msg.tprint(msg)

Uface = store_unknown('Unknown faces', 'rename me please') # Store Unknown faces for proof or addition to library

My_msg.tprint("(Re)written by Harry de Bont. ")
My_msg.tprint("2022")
My_msg.tprint("Face recognition starting. This will take a while, please be patient.")
My_msg.tprint(str("Using open_CV_version: "+cv2.__version__))


# Encode faces from a folder
sfr = SimpleFacerec()
#sfr.load_encoding_images(image_dir)
sfr.load_encoding_images(image_path)
# Load Camera
#cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # USB cam
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW) # Center Cam

# Create Registration Face Recognition
RFR = register_faceR()

while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        name = undouble(name)
        if name != 'Unknown':                                                                                       
            cv2.putText(frame, name,(x1, y2 + 25), cv2.FONT_HERSHEY_DUPLEX, 1, (200, 200, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4) 
        else:
            # No rectangle on a unknown face not to obscure use for later training
            cv2.putText(frame, name,(x1, y2 + 125), cv2.FONT_HERSHEY_DUPLEX, 1, (200, 200, 200), 2)
            Uface.save_frame(frame) # Faulty code no unknown faces is saved to file..... check unknown_faces routine
        RFR.register(name)
            

    cv2.imshow("Face recognition", frame)
    
    key = cv2.waitKey(1)
    if key == 27:   # quit program with ESC key pressed
        RFR.registryWrite(True) # Store registration to file
        break

cap.release()
cv2.destroyAllWindows()