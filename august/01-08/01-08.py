def solve_magic_square(grid):

    position = None
    row_sum = []

    for row in grid:
        row_sum.append(sum(row))
    

    print(row_sum)



    return grid

# Tests:
solve_magic_square([[2, 7, 6], [9, 0, 1], [4, 3, 8]]) #should return 5.
solve_magic_square([[0, 14, 12], [18, 10, 2], [8, 6, 16]]) #should return 4.
solve_magic_square([[12, 17, 16], [19, 0, 10], [14, 13, 18]]) #should return "impossible".
solve_magic_square([[15, 35, 31], [43, 27, 11], [23, 19, 0]]) #should return 39.
solve_magic_square([[26, 41, 14], [47, 35, 0], [32, 29, 44]]) #should return "impossible".