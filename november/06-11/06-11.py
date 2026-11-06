from datetime import date

def get_weekday(date_string):

    d = date.fromisoformat(date_string)
    day_of_week = d.strftime("%A")

    print(day_of_week)

    return day_of_week

## Tests:
get_weekday("2025-11-06") #should return Thursday.
get_weekday("1999-12-31") #should return Friday.
get_weekday("1111-11-11") #should return Saturday.
get_weekday("2112-12-21") #should return Wednesday.
get_weekday("2345-10-01") #should return Monday.