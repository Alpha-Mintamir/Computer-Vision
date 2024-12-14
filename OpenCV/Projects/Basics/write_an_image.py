import numpy as np
import cv2
# Load a color image in grayscale
img = cv2.imread('C:/Users/Admin/OneDrive/Pictures/5811995091668156460_99.jpg',0)


result = cv2.imwrite('C:/Computer Vision/OpenCV/Images/result.png', img)\

if result:
    print('Image saved successfully')
else:
    print('Error in saving image')