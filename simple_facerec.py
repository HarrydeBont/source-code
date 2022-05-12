import face_recognition
import directory_structure
import cv2
import os
import glob
import numpy as np
from objectR_handler import objecter
from ObjectHasher import ObjectHash
from PIL import Image


class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

        # Resize frame for a faster speed
        self.frame_resizing = 0.25
        self.trained_faces = objecter('FaceR model', 'Home security faces')
        self.trained_names = objecter('FaceR model', 'Home security names')

        self.MyObjHash = ObjectHash() 

        dir_model = 'directory hash'
        model_file = 'hash'
        self.new_hash = objecter(dir_model, model_file)

    def load_encoding_images(self, images_path):
        """
        Load encoding images from path
        :param images_path:
        :return:
        """
        # Load Images
        dir_images = directory_structure.dir_struc()
        
        print("{} stored faces found.".format(dir_images.count_faces()))
        if not(self.MyObjHash.checkImage()): # When False re-train the model
            print("Re-training the model.")
            # Store image encoding and names
            for img_path in images_path:
                img = cv2.imread(img_path)
                img_check = Image.fromarray(img)              # check if color coding is RGB or BGR
                print(img_path)
                print(img_check.mode)
                rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                # Get the filename only from the initial file path.
                basename = os.path.basename(img_path)
                (filename, ext) = os.path.splitext(basename)
                # Get encoding
                img_encoding = face_recognition.face_encodings(rgb_img)[0]

                # Store file name and file encoding
                self.known_face_encodings.append(img_encoding)
                self.known_face_names.append(filename)
            # Write trained model to physical drive
            self.trained_faces.write_model(self.known_face_encodings)
            self.trained_names.write_model(self.known_face_names)
            # print("Trained model: ", self.known_face_encodings)
            print("Neural net of images trained and saved.")
            # Write a new image hash since the images directory has been changed
            self.new_hash.write_model(self.MyObjHash.CalcImageHash())

        else:
            self.known_face_encodings = self.trained_faces.read_model()
            self.known_face_names = self.trained_names.read_model()
            print("Neural net of images is re-loaded.")


    def detect_known_faces(self, frame):
        """
        Find all the faces and face encodings in the current frame of video
        Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        """
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
            face_names.append(name)

        # Convert to numpy array to adjust coordinates with frame resizing quickly
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names
