import cv2
import imutils
import numpy as np
gambar = cv2.imread("C:\\Users\\LENOVO\\praxisAI\\02-01-basic\\images.jpeg")

# # h,w,d = gambar.shape
# print("image size:", h, w, d)

# cv2.imshow("meme", gambar)
# cv2.waitKey(0)

# resized = cv2.resize(gambar, (400, 400))
# cv2.imshow("meme", resized)
# cv2.waitKey(0)

# crp = gambar[100:150, 100:150]
# cv2.imshow("ROI", crp)
# cv2.waitKey(0)

# rotated = imutils.rotate(gambar, -45)
# cv2.imshow("Imutils Rotation", rotated)
# cv2.waitKey(0)

# blurred = cv2.GaussianBlur(gambar, (11, 11), 0)
# cv2.imshow("Blurred", blurred)
# cv2.waitKey(0)

# output = gambar.copy()
# cv2.rectangle(output, (750, 150), (85, 750), (255, 0, 0), 9)
# cv2.imshow("Circle", output)
# cv2.waitKey(0)

output = gambar.copy()
cv2.line(output, (90, 100), (400, 400), (0, 0, 255), 5)
cv2.line(output, (100, 200), (400, 400), (0, 0, 255), 5)
cv2.imshow("Line", output)
cv2.waitKey(0)

# output = gambar.copy()
# cv2.putText(output, "uang 10rb", (10, 25), 
# cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
# cv2.imshow("Text", output)
# cv2.waitKey(0)