def second_largest(arr):

    #sort array
    arr.sort()
    sort_list = []

    for element in arr:
        if(element not in sort_list):
            sort_list.append(element)

    second = sort_list[len(sort_list)-2]
    print(second)

    return second

#Tests:
second_largest([1, 2, 3, 4]) #should return 3.
second_largest([20, 139, 94, 67, 31]) #should return 94.
second_largest([2, 3, 4, 6, 6]) #should return 4.
second_largest([10, -17, 55.5, 44, 91, 0]) #should return 55.5.
second_largest([1, 0, -1, 0, 1, 0, -1, 1, 0]) #should return 0.