def is_mirror(str1, str2):

    clean_str1 = ''.join(filter(str.isalnum, str1))
    clean_str2 = ''.join(filter(str.isalnum, str2))
    clean_str2 = clean_str2[::-1]

    if(clean_str1 == clean_str2):
        return True
    else:
        return False

    

is_mirror("helloworld", "helloworld") #should return Fals
is_mirror("Hello World", "dlroW olleH") #should return True.
is_mirror("RaceCar", "raCecaR") #should return True.
is_mirror("RaceCar", "RaceCar") #should return False.
is_mirror("Mirror", "rorrim") #should return False.
is_mirror("Hello World", "dlroW-olleH") #should return True.
is_mirror("Hello World", "!dlroW !olleH") #should return True.