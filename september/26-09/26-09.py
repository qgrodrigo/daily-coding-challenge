def speeding(speeds, limit):

    count = 0
    count_exces = 0
    average = 0
    answer_list = []

    for i in speeds:
        if(i > limit):
            count += 1
            count_exces += (i - limit)

    if(count == 0):
        answer_list = [0,0]
    else:

        average = count_exces / count
        answer_list = [count, average]
    print(count)
    print(average)
    print('----------')

    return answer_list

#Tests:
speeding([50, 60, 55], 60) #should return [0, 0].
speeding([58, 50, 60, 55], 55) #should return [2, 4].
speeding([61, 81, 74, 88, 65, 71, 68], 70) #should return [4, 8.5].
speeding([100, 105, 95, 102], 100) #should return [2, 3.5].
speeding([40, 45, 44, 50, 112, 39], 55) #should return [1, 57].