def find_landing_spot(matrix):

    rows = len(matrix)
    columns = len(matrix[0])
    neighbors = []
    positions = []
    
    for i in range(rows):
        for j in range(columns):
            if(matrix[i][j] == 0):
                #print(f'cero encontrado en position: {i},{j}')
                position = [i,j]
                right = 0
                left = 0
                up = 0
                down = 0

                if j < len(matrix[0]) - 1:
                    right = matrix[i][j+1]
                if j > 0:
                    left = matrix[i][j-1]
                if i > 0:
                    up = matrix[i-1][j]
                if i < len(matrix) -1:
                    down = matrix[i+1][j]

                sum = right + left + up + down

                neighbors.append(sum)
                positions.append(position)

    less_number_position = neighbors.index(min(neighbors))

    safest_landing_position = positions[less_number_position]

    print(safest_landing_position)


    return safest_landing_position

#Tests:
find_landing_spot([[1, 0], [2, 0]]) #should return [0, 1].
find_landing_spot([[9, 0, 3], [7, 0, 4], [8, 0, 5]]) #should return [1, 1].
find_landing_spot([[1, 2, 1], [0, 0, 2], [3, 0, 0]]) #should return [2, 2].
find_landing_spot([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]]) #should return [2, 1].