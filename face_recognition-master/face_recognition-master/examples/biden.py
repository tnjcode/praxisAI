# from PIL import Image
import cv2
import face_recognition

# Load the jpg file into a numpy array
image_disp = cv2.imread("biden.jpg")
image = face_recognition.load_image_file("biden.jpg")

cv2.imshow("image", image_disp)
cv2.waitKey(0)

# Find all the faces in the image using the default HOG-based model.
# This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
# See also: find_faces_in_picture_cnn.py
face_locations = face_recognition.face_locations(image) 

print(face_locations)
top, right, bottom, left = face_locations[0]

    # You can access the actual face itself like this:
img_dsp = cv2.rectangle(image_disp, (left, top), (right, bottom), (255, 0, 0), 2)
cv2.imshow("Face", image_disp)
cv2.waitKey(0)