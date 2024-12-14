import numpy as np
import cv2
# Load a color image in grayscale
img = cv2.imread('C:/Users/Admin/OneDrive/Pictures/5811995091668156460_99.jpg',1)

# split function

r,g,b = cv2.split(img)
cv2.imshow('Red',r)

#cv2.imshow('Green',g)

#cv2.imshow('Blue',b)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# merge function
merged_img = cv2.merge((r, g, b))
cv2.imshow('Merged Image', merged_img)

cv2.waitKey(0)
cv2.destroyAllWindows()