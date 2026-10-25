def dive(map, coordinates):

    x_position = coordinates[0]
    y_position = coordinates[-1]

    count_value_O = 0
    positions = []
            
    for i, sublista in enumerate(map):
        for j, elemento in enumerate(sublista):
            if elemento == 'O':   
                count_value_O += 1
                positions.append([i,j])
            
    if coordinates in positions and len(positions) > 1:
        print('Found')
        return 'Found' 

    if coordinates in positions and len(positions) == 1:
        print('Recovered')
        return 'Recovered'
          
    if map[x_position][y_position] == "-":
        print('Empty')
        return 'Empty'
    if map[x_position][y_position] == "X":
        print('Found')
        return 'Found'



#Tests:
dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 1]) #should return "Recovered".
dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 0]) #should return "Empty".
dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1]) #should return "Found".
dive([[ "-", "-", "-"], [ "X", "O", "X"], [ "-", "-", "-"]], [1, 2]) #should return "Found".
dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [2, 0]) #should return "Recovered".
dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [1, 2]) #should return "Empty".