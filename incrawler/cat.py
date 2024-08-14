import cv2
import numpy as np

################################################################
path = 'C:\\Users\\LENOVO\\praxisAI\\haarcascad\\classifier\\cascade.xml'  # PATH OF THE CASCADE
cameraNo = 0                       # CAMERA NUMBER
objectName = 'Bola'                # OBJECT NAME TO DISPLAY
frameWidth= 640                    # DISPLAY WIDTH
frameHeight = 480                  # DISPLAY HEIGHT
color= (255,0,255)                 # COLOR OF DETECTION BOX
#################################################################

cap = cv2.VideoCapture(cameraNo)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

def empty(a):
    pass

# CREATE TRACKBAR
cv2.namedWindow("Result")
cv2.resizeWindow("Result",frameWidth,frameHeight+100)
cv2.createTrackbar("Scale","Result",400,1000,empty)
cv2.createTrackbar("Neig","Result",8,50,empty)
cv2.createTrackbar("Min Area","Result",5000,100000,empty)
cv2.createTrackbar("Brightness","Result",180,255,empty)

# LOAD THE CLASSIFIERS DOWNLOADED
cascade = cv2.CascadeClassifier(path)

while True:
    # SET CAMERA BRIGHTNESS FROM TRACKBAR VALUE
    cameraBrightness = cv2.getTrackbarPos("Brightness", "Result")
    cap.set(10, cameraBrightness)
    # GET CAMERA IMAGE AND CONVERT TO GRAYSCALE
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # DETECT THE OBJECT USING THE CASCADE
    scaleVal = 1 + (cv2.getTrackbarPos("Scale", "Result") / 1000)
    neig = cv2.getTrackbarPos("Neig", "Result")
    objects = cascade.detectMultiScale(gray, scaleVal, neig)
    
    # Filter objects based on multiple colors
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define color ranges for blue, pinkish red, yellow, and orange
    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([130, 255, 255])

    lower_pink_red = np.array([160, 50, 50])
    upper_pink_red = np.array([180, 255, 255])

    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    lower_orange = np.array([10, 100, 100])
    upper_orange = np.array([20, 255, 255])

    # Create masks for each color
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_pink_red = cv2.inRange(hsv, lower_pink_red, upper_pink_red)
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask_orange = cv2.inRange(hsv, lower_orange, upper_orange)

    # Combine all masks
    combined_mask = cv2.bitwise_or(mask_blue, mask_pink_red)
    combined_mask = cv2.bitwise_or(combined_mask, mask_yellow)
    combined_mask = cv2.bitwise_or(combined_mask, mask_orange)
    
    # DISPLAY THE DETECTED OBJECTS
    for (x, y, w, h) in objects:
        area = w * h
        minArea = cv2.getTrackbarPos("Min Area", "Result")
        if area > minArea:
            roi_color = img[y:y+h, x:x+w]
            roi_mask = combined_mask[y:y+h, x:x+w]
            if cv2.countNonZero(roi_mask) > 0.5 * area:  # More than 50% of the detected region is the ball's color
                cv2.rectangle(img, (x, y), (x+w, y+h), color, 3)
                cv2.putText(img, objectName, (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)

    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
