import numpy as np
import cv2
# Load a color image in grayscale
img = cv2.imread('C:/Users/Admin/OneDrive/Pictures/5811995091668156460_99.jpg',0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()