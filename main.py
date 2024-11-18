import cv2 as cv
import sys
 
img = cv.imread("starry_night.png")
 
if img is None:
    sys.exit("Could not read the image.")
 
cv.imshow("Display window", img)
k = cv.waitKey(0)

print(img.shape)

if k == ord("s"):
    cv.imwrite("starry_night.jpg", img)
    