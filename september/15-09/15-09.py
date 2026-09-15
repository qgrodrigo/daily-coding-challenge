def adjust_thermostat(temp, target):

    adjust = ''

    if(temp < target):
        adjust = 'heat'
    elif(temp > target):
        adjust = 'cool'
    else:
        adjust = 'hold'

    print(adjust)

    return adjust

adjust_thermostat(0.0, 0.0) #should return "hold".