# import argparse
# import imutils
# import cv2
# import numpy as np
# # construct the argument parser and parse the arguments
# # ap = argparse.ArgumentParser()
# # ap.add_argument("-i", "--image", required=True,
# # 	help="path to input image")
# # args = vars(ap.parse_args())

# image = cv2.imread("C:\\Users\\LENOVO\\praxisAI\\01-04-detect\\screws.jpg")
# cv2.imshow("Image", image)
# cv2.waitKey(0)
# # convert the image to grayscale

# # blurred = cv2.GaussianBlur(image, (11, 11), 0)
# # cv2.imshow("Blurred", blurred)
# # cv2.waitKey(0)


# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray", gray)
# cv2.waitKey(0)


# edged = cv2.Canny(image, 30, 150)
# cv2.imshow("Edged", edged)
# cv2.waitKey(0)

# thresh = cv2.threshold(image, 225, 255, cv2.THRESH_BINARY_INV)[1]
# cv2.imshow("Thresh", thresh)
# cv2.waitKey(0)

# cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
# 	cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
# output = image.copy()
# # loop over the contours

# # 	# draw each contour on the output image with a 3px thick purple
# # 	# outline, then display the output contours one at a time
# cv2.drawContours(output, cnts, -1, (240, 0, 159), 3)
# cv2.imshow("Contours", output)
# cv2.waitKey(0)
	
# text = "I found {} objects!".format(len(cnts))
# cv2.putText(output, text, (1, 65),  cv2.FONT_HERSHEY_SIMPLEX, 0.9,
# 	(240, 0, 159), 2)
# cv2.imshow("Contours", output)
# cv2.waitKey(0)

# # construct the argument parse and parse the arguments


import cv2
import imutils

# Load the image
image = cv2.imread("C:\\Users\\LENOVO\\praxisAI\\01-04-detect\\mur.jpeg")
cv2.imshow("Image", image)
cv2.waitKey(0)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

# Apply edge detection
edged = cv2.Canny(gray, 30, 150)  # Apply Canny on grayscale image
cv2.imshow("Edged", edged)
cv2.waitKey(0)

# Apply thresholding on the grayscale image
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

# Find contours
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = image.copy()

# Draw contours on the output image
cv2.drawContours(output, cnts, -1, (240, 0, 159), 3)
cv2.imshow("Contours", output)
cv2.waitKey(0)
	
# Add text to the output image
text = "I found {} objects!".format(len(cnts))
cv2.putText(output, text, (1, 65),  cv2.FONT_HERSHEY_SIMPLEX, 0.9,
	(240, 0, 159), 2)
cv2.imshow("Contours", output)
cv2.waitKey(0)
