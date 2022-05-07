# test main function

# This program is an attempt to program a FACE RECOGNITION ready for home automation
# Author: Harry de Bont 2022
# Version history / To do next: 
# 1) Re-load previously trained model when no pictures have been added. done V 15-4-2022
# 2) Hashing_images and Hash_calculate in one Class done V 19-04-2022 (ObjectHasher)
# 3) Make a Register library-routine  done V 25-04-2022 (F_rec_register)
# 4) Save images of non-recognized faces done V 29-04-2022 (Unknown_faces)
# 5) Use saved image as training input done V 29-04-2022 (works without changes)
# 6) Create multiple photo-entries for one person done V 29-04-2022 (undoubling)
# 7) Move face images to root directory as well (D:/Python) done V 29-04-2022 (directory_structure)
# 8) Make a routine for copying unknown faced to images (supervised so need to use UI)
# 9) Create user interace
# 10) Make executable


def main():
    print("Test main function!")
    from tkinter import image_types
    import cv2
    import datetime
    from F_rec_register import register_faceR
    from unknown_faces import store_unknown
    from undoubling import undouble
    from directory_structure import root_dir
    import os

    main_root_dir = root_dir()
    image_path = "images"
    image_dir = os.path.join(main_root_dir, image_path)

    Uface = store_unknown('Unknown faces', 'Who is this') # Store Unknown faces for proof or addition to library

    print("(Re)written by Harry de Bont. ", end= '')
    print("2022")
    print("Face recognition starting. This will take a while, please be patient.")
    print("Using open_CV_version: ", cv2.__version__)
    from simple_facerec import SimpleFacerec

    # Encode faces from a folder
    sfr = SimpleFacerec()
    sfr.load_encoding_images(image_dir)

    # Load Camera
    cap = cv2.VideoCapture(2) # Center Cam

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
                

        # cv2.imshow("Face recognition", frame)
        
        key = cv2.waitKey(1)
        if key == 27:   # quit program with ESC key pressed
            RFR.registryWrite(True) # Store registration to file
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()