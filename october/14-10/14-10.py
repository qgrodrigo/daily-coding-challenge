def count(text, parameter):

    text = ''.join(text.split())
    count = 0

    for i in range(len(text) -len(parameter)+1):
        if(text[i:i+len(parameter)] == parameter):
            count += 1

    print(count)

    return count

#Tests:
count('abcdefg', 'def') #should return 1.
count('hello', 'world') #should return 0.
count('mississippi', 'iss') #should return 2.
count('she sells seashells by the seashore', 'sh') #should return 3.
count('101010101010101010101', '101') #should return 10.