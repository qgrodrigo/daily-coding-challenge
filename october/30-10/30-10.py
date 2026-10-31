def nth_prime(n):

    count_primes = 0
    index = 1
    last_prime = 0

    while count_primes < n:
        if is_prime(index):
            count_primes += 1
            last_prime = index

        index += 1

    print(last_prime)
    
    return n
        
def is_prime(number) -> bool:
    is_prime = True

    if number <= 1:
        is_prime = False

    for i in range(2, number-1 ):
        if number % i == 0:
            is_prime = False
            break
        else:
            continue

    #print(f'n is prime: {is_prime}')

    return is_prime


## Tests:
nth_prime(5) #should return 11.
nth_prime(10) #should return 29.
nth_prime(16) #should return 53.
nth_prime(99) #should return 523.
nth_prime(1000) #should return 7919.