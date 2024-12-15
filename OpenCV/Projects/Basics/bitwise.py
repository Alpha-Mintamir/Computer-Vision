import cv2
import numpy as np


def bitwise_example1():
    img1 = cv2.imread('C:/Computer Vision/OpenCV/Images/unfilledCircle.jpg')
    img2 = cv2.imread('C:/Computer Vision/OpenCV/Images/filledCircle.png')

    if img1 is None or img2 is None:
        print('Could not open or find the images.')
        exit()

    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    dest1 = cv2.bitwise_and(img2, img1, mask=None)
    dest2 = cv2.bitwise_or(img2, img1, mask=None)
    dest3 = cv2.bitwise_xor(img1, img2, mask=None)
    cv2.imshow('A', img1)
    cv2.imshow('B', img2)
    cv2.imshow('AND', dest1)
    cv2.imshow('OR', dest2)
    cv2.imshow('XOR', dest3)
    cv2.imshow('NOT A', cv2.bitwise_not(img1))
    cv2.imshow('NOT B', cv2.bitwise_not(img2))
    if cv2.waitKey(0) & 0xFF == 27:
        cv2.destroyAllWindows()

# bitwise_example1()

def bitwise_example2():
    img1 = cv2.imread('C:/Computer Vision/OpenCV/Images/Mark-Zuckerberg-2019.png')
    img2 = cv2.imread('C:/Computer Vision/OpenCV/Images/openCV_logo.png')
    rows, cols, channels = img2.shape
    roi = img1[0:rows, 0:cols]
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    # Now black-out the area of logo
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    # Take only region of logo from logo image.
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
    # Put logo in ROI
    dst = cv2.add(img2_fg, img1_bg)
    img1[0:rows, 0:cols] = dst
    cv2.imshow('Result', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

bitwise_example2()