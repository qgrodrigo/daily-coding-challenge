def format(seconds):

    time_formated = ''
    hours_text = ''
    minutes_text = ''
    seconds_text = ''

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds_rest = (seconds % 3600) % 60

    if seconds_rest < 10:
        seconds_text = f'0{seconds_rest}'
    else:
        seconds_text = seconds_rest

    if minutes < 0:
        minutes_text = '0'
    elif minutes > 0 and minutes < 10:
        if hours < 1:
            minutes_text = f'{minutes}'
        else: 
            minutes_text = f'0{minutes}'
    else:
        minutes_text = minutes

    if hours > 0:
        hours_text = f'{hours}:'

    time_formated = f'{hours_text}{minutes_text}:{seconds_text}' 

    print(time_formated)
    
    return time_formated

#Tests:
format(500) #should return "8:20".
format(4000) #should return "1:06:40".
format(1) #should return "0:01".
format(5555) #should return "1:32:35".
format(99999) #should return "27:46:39".