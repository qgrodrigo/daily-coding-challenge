from datetime import date

def days_until_weekend(date_string):

    d = date.fromisoformat(date_string)
    WEEKEND = [5, 6]

    message = ''

    if d.weekday() in WEEKEND:
        message = "It's the weekend!"
    else:
        days_to_weekend = 5 - d.weekday() 
        if days_to_weekend == 1:
            message = f'{days_to_weekend} day until the weekend.'
        else:
            message = f'{days_to_weekend} days until the weekend.'
    
    print(message)

    return message

## Tests:
days_until_weekend("2025-11-14") #should return "1 day until the weekend.".
days_until_weekend("2025-01-01") #should return "3 days until the weekend.".
days_until_weekend("2025-12-06") #should return "It's the weekend!".
days_until_weekend("2026-01-27") #should return "4 days until the weekend.".
days_until_weekend("2026-09-07") #should return "5 days until the weekend.".
days_until_weekend("2026-11-29") #should return "It's the weekend!".