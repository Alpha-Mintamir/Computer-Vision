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




# mouse callback function
drawing = True
shape = 'r'
def draw_circle(event, x, y, flags, param):
    global x1, x2
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        x1, x2 = x, y
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if shape == 'r':
            cv.rectangle(img, (x1, x2), (x, y), (0, 255, 0), -1)
        if shape == 'l':
            cv.line(img, (x1, x2), (x, y), (255, 255, 255), 3)
        if shape == 'c':
            cv.circle(img, (x, y), 10, (255, 255, 0), -1)
img = cv.imread('lena.jpg')
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)
while(1):
    cv.imshow('image', img)
    key = cv.waitKey(1)
    if key == ord('1'):
        shape = 'r'
    if key == ord('2'):
        shape = 'l'
    if key == ord('3'):
        shape = 'c'
#print (shape)