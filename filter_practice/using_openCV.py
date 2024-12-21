import cv2
import numpy as np

# Load the image
image = cv2.imread('C:/Computer Vision/OpenCV/Images/5811995091668156460_99.jpg', 0)

# Create a kernel
kernel = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])

# pad the image
padded_image = np.pad(image, 1, mode='constant')

# Apply the filter to the image
result_image = np.zeros((len(image), len(image[0])))
for i in range(len(image)):
    for j in range(len(image[0])):
        result_image[i, j] = np.sum(padded_image[i:i+len(kernel), j:j+len(kernel[0])] * kernel)

# Display the image
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', result_image.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()