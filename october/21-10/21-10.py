def adjust_thermostat(current_f, target_c):

    target_c_to_f = (target_c * 1.8) + 32

    if (current_f == target_c_to_f):
        return 'Hold'
    if(current_f < target_c_to_f):
        return f'Heat: {round(target_c_to_f - current_f, 1)} degrees Fahrenheit'
    
    if(current_f > target_c_to_f):
        return f'Cool: {round(current_f  - target_c_to_f,1)} degrees Fahrenheit'    


#Tests:
print(adjust_thermostat(32, 0)) #should return "Hold".
print(adjust_thermostat(70, 25)) #should return "Heat: 7.0 degrees Fahrenheit".
print(adjust_thermostat(72, 18)) #should return "Cool: 7.6 degrees Fahrenheit".
adjust_thermostat(212, 100) #should return "Hold".
adjust_thermostat(59, 22) #should return "Heat: 12.6 degrees Fahrenheit".