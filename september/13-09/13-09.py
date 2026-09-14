def find_missing_numbers(arr):

    big_number = max(arr)
    missing_numbers = []

    for i in range(big_number):
        number = i+1
        if number not in arr:
            missing_numbers.append(number)

    return missing_numbers


find_missing_numbers([1, 2, 3, 4, 5]) # should return [].
find_missing_numbers([10, 1, 10, 1, 10, 1]) #should return [2, 3, 4, 5, 6, 7, 8, 9].