import cv2
import numpy as np


img1 = cv2.imread('C:/Computer Vision/OpenCV/Images/unfilledCircle.jpg')
img2 = cv2.imread('C:/Computer Vision/OpenCV/Images/filledCircle.png')

if img1 is None or img2 is None:
    print('Could not open or find the images.')
    exit()

if img1.shape != img2.shape:
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
dest1 = cv2.bitwise_and(img2, img1, mask = None)
dest2 = cv2.bitwise_or(img2, img1, mask = None)
dest3 = cv2.bitwise_xor(img1, img2, mask = None)
cv2.imshow('A', img1)
cv2.imshow('B', img2)
cv2.imshow('AND', dest1)
cv2.imshow('OR', dest2)
cv2.imshow('XOR', dest3)
cv2.imshow('NOT A', cv2.bitwise_not(img1))
cv2.imshow('NOT B', cv2.bitwise_not(img2))
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()