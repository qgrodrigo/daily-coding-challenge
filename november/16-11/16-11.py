def count_rectangles(width, height):

    count = (width * (width + 1) / 2) * (height * (height + 1) / 2)
    print(int(count))
    return int(count)

## Tests:
count_rectangles(1, 3) #should return 6.
count_rectangles(3, 2) #should return 18.
count_rectangles(1, 2) #should return 3.
count_rectangles(5, 4) #should return 150.
count_rectangles(11, 19) #should return 12540.