# test module unknwon faces
from unknown_faces import store_unknown
import cv2

tuf = store_unknown('Unknown faces', 'Who is this 0001.jpg') # Test Unknown faces
frame = cv2.imread("C:/Users/HWdeB/Documents/Python/source facerecogn/source code/images/Fabian de Bont.jpg")
tuf.save_frame(frame)