def sequence(n):

    number_sequence = ''

    for i in range(1, n+1):
        number_sequence += str(i)

    print(number_sequence)
    return number_sequence

#Tests
sequence(5) #should return "12345".
sequence(10) #should return "12345678910".
sequence(1) #should return "1".
sequence(27) #should return "123456789101112131415161718192021222324252627".