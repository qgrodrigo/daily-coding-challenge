def build_matrix(rows, cols):

    filled_matrix = []
    row = [0] * cols

    for i in range(rows):
        filled_matrix.append(row)

    print(filled_matrix)
    
    return filled_matrix

build_matrix(2, 3) #should return [[0, 0, 0], [0, 0, 0]].
build_matrix(3, 2) #should return [[0, 0], [0, 0], [0, 0]].
build_matrix(4, 3) #should return [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]].
build_matrix(9, 1) #should return [[0], [0], [0], [0], [0], [0], [0], [0], [0]].