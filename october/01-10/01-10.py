def to_decimal(binary):

    binary = binary[::-1]
    decimal = 0
    for i in range(len(binary)):

        decimal += int(binary[i]) * (2 ** i)

    print(decimal)

    return decimal

to_decimal("101") #should return 5.
to_decimal("1010") #should return 10.
to_decimal("10010") #should return 18.
to_decimal("1010101") #should return 85.