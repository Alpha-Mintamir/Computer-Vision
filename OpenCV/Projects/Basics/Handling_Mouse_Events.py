import numpy as np
import cv2 as cv

def drawfunction(event, x, y, flags, param):
    global img
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 20, (255, 255, 255), -1)

# mouse callback function
img = cv.imread('C:/Users/Admin/OneDrive/Pictures/5811995091668156460_99.jpg')
cv.namedWindow('image')
cv.setMouseCallback('image', drawfunction)

while(1):
    cv.imshow('image', img)
    key = cv.waitKey(1)
    if key == 27:
        break
cv.destroyAllWindows()