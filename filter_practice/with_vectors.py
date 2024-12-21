# we start with 5 * 5 matrix
# we will filter the matrix with 3 * 3 filter(kernel)(mask)

vector = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
kernel = [[1,0,-1],[1,0,-1],[1,0,-1]]

# we add padding to the matrix

def add_padding(vector):
    #upper padding
    vector.insert(0, [0,0,0,0,0,0,0])
    
    #lower padding
    vector.append([0,0,0,0,0,0,0])
    
    #left and right padding
    for i in range (1, len(vector)-1):
        vector[i].insert(0,0)
        vector[i].append(0)
        
    return vector

# we will apply the filter to the matrix

#since we have now 7 * 7 matrix with the padding. 

result_matrix = []

# Apply the filter to the matrix
padded_vector = add_padding(vector)
for i in range(1, len(padded_vector) - 1):
    row = []
    for j in range(1, len(padded_vector[i]) - 1):
        result = 0
        for m in range(len(kernel)):
            for n in range(len(kernel[m])):
                result += padded_vector[i - 1 + m][j - 1 + n] * kernel[m][n]
        row.append(result)
    result_matrix.append(row)

for row in result_matrix:
    print(row)


