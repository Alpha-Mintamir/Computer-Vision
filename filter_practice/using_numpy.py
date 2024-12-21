import numpy as np

# Create a numpy array
vector = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
kernel = np.array([[1,0,-1],[1,0,-1],[1,0,-1]])

# Add padding to the matrix
padded_vector = np.pad(vector,1, mode='constant')

# Apply the filter to the matrix
result_matrix = np.zeros((len(vector), len(vector[0])))
for i in range(len(vector)):
    for j in range(len(vector[0])):
        result_matrix[i][j] = np.sum(padded_vector[i:i+len(kernel), j:j+len(kernel[0])] * kernel)

print(result_matrix)