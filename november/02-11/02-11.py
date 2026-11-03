import math

def infected(days):

    infected_count = 1


    for i in range(1, days + 1):
        infected_count *= 2
        if i % 3 == 0:
            patch_number = math.ceil(infected_count * 0.2)
            infected_count -= patch_number 

    print(infected_count)
    return infected_count

## Tests:
infected(1) #should return 2.
infected(3) #should return 6.
infected(8) #should return 152.
infected(17) #should return 39808.
infected(25) #should return 5217638.