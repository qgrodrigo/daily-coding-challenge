def fibonacci_sequence(start_sequence, length):

    if length <= 0:
        return []

    i = 0

    fibonacci(start_sequence[0])

    return 0

def fibonacci(number: int):

    fibo_searched = 0
    index = 0
    while fibo_searched != number:
        fibo_searched += fibo_searched
        index += 1

    print(fibo_searched)
    print(index)

## Tests:
fibonacci_sequence([0, 1], 20) #should return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181].
fibonacci_sequence([21, 32], 1) #should return [21].
fibonacci_sequence([0, 1], 0) #should return [].
fibonacci_sequence([10, 20], 2) #should return [10, 20].
fibonacci_sequence([123456789, 987654321], 5) #should return [123456789, 987654321, 1111111110, 2098765431, 3209876541].