def to_12(time):

    hour = int(time[:2])
    minutes = time[2:]
    hour_to_12 = 0

    if(hour > 12):
        hour_to_12 = str(hour - 12) + ':' + minutes + ' PM'

    if( hour < 12):
        
        if(hour == 0):
                hour_to_12 = str(12) + ':' + minutes + ' AM'
        else:    
            hour_to_12 = str(hour) + ':' + minutes + ' AM'

    

    print(hour_to_12)
    #print(minutes)

    return hour_to_12

to_12("1124") #should return "11:24 AM".
to_12("0900") #should return "9:00 AM".
to_12("1455") #should return "2:55 PM".
to_12("2346") #should return "11:46 PM".
to_12("0030") #should return "12:30 AM".