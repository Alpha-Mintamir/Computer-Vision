import numpy as np
import cv2
# Load a color image in grayscale
img = cv2.imread('C:/Users/Admin/OneDrive/Pictures/5811995091668156460_99.jpg',1)

shape = img.shape
size = img.size
#print(size)
#print(shape)

p = img[50,50]

#print(p)


#lets change the color of the first 100*100 pixels to blank

def change_color_to_blank(img, width, height):
    for i in range(width):
        for j in range(height):
            img[i, j] = [0, 0, 0]
    return img

#img = change_color_to_blank(img, 100, 100)
#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

