def rotate(matrix):
    
    n = len(matrix)
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[j][n - 1 - i] = matrix[i][j]

    print(result)
    return result

rotate([[1]]) #should return [[1]].
rotate([[1, 2], [3, 4]]) #should return [[3, 1], [4, 2]].
rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) #should return [[7, 4, 1], [8, 5, 2], [9, 6, 3]].
rotate([[0, 1, 0], [1, 0, 1], [0, 0, 0]]) #should return [[0, 1, 0], [0, 0, 1], [0, 1, 0]].