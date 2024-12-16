import numpy as np
import cv2
img = cv2.imread('C:/Users/Admin/OneDrive/Pictures/5811995091668156460_99.jpg',1)
txt="Lionel Messi"
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,txt,(10,100), font, 2,(255,255,255),2,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()