# Weekday Finder
Given a string date in the format YYYY-MM-DD, return the day of the week.

Valid return days are:

"Sunday"
"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
Be sure to ignore time zones.

## Tests:
get_weekday("2025-11-06") should return Thursday.
get_weekday("1999-12-31") should return Friday.
get_weekday("1111-11-11") should return Saturday.
get_weekday("2112-12-21") should return Wednesday.
get_weekday("2345-10-01") should return Monday.