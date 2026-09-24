def is_perfect_square(n):

    is_perfect = False
    square = pow(n, 0.5)

    if(n >= 0):
        if(square.is_integer()):
            is_perfect = True
        else:
            is_perfect = False
    else:
        is_perfect = False

    print(is_perfect)
    return is_perfect

is_perfect_square(9) #should return True.
is_perfect_square(49) #should return True.
is_perfect_square(1) #should return True.
is_perfect_square(2) #should return False.
is_perfect_square(99) #should return False.
is_perfect_square(-9) #should return False.
is_perfect_square(0) #should return True.
is_perfect_square(25281) #should return True.