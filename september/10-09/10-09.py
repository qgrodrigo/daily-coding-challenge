def array_diff(arr1, arr2):

    array_diff = []

    for element in arr1:
        if element not in arr2:
            array_diff.append(element)

    for element_two in arr2:
        if element_two not in arr1:
            array_diff.append(element_two)

    

    #ordenar el array
    array_diff.sort()

    for element in array_diff:
        print(element)

    return array_diff


#array_diff(["apple", "banana"], ["apple", "banana", "cherry"]) 
array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"])