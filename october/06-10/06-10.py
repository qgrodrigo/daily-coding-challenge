def send_message(route):

    time = 0
    speed = 300000

    for distance in route:

        time += (distance / speed)

    time += (len(route) -1) * 0.5
    print()

    return round(time, 4)

send_message([300000, 300000]) #should return 2.5.
send_message([384400, 384400]) #should return 3.0627.
send_message([54600000, 54600000]) #should return 364.5.
send_message([1000000, 500000000, 1000000]) #should return 1674.3333.
send_message([10000, 21339, 50000, 31243, 10000]) #should return 2.4086.
send_message([802101, 725994, 112808, 3625770, 481239]) #should return 21.1597.