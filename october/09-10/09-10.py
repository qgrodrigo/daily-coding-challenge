import time

def moon_phase(date_string):

    base_date = time.mktime(time.strptime("2000-01-06", "%Y-%m-%d"))
    to_date = time.mktime(time.strptime(date_string, "%Y-%m-%d"))
    diference_days = (to_date - base_date) / 86400
    phase = ''

    days = diference_days % 28 +1
    #print(days)
    
    if(days >= 1 and days <= 7):
        phase = 'New'
    if(days >= 8 and days <= 14):
            phase = 'Waxing'
    if(days >= 15 and days <= 21):
                phase = 'Full'
    if(days >= 22 and days <= 28):
                phase = 'Waning'

    
    #print(phase)

    return phase



#Tests:
moon_phase("2000-01-12") #should return "New".
moon_phase("2000-01-13") #should return "Waxing".
moon_phase("2014-10-15") #should return "Full".
moon_phase("2012-10-21") #should return "Waning".
moon_phase("2022-12-14") #should return "New".