Duration Formatter
Given an integer number of seconds, return a string representing the same duration in the format "H:MM:SS", where "H" is the number of hours, "MM" is the number of minutes, and "SS" is the number of seconds. Return the time using the following rules:

Seconds: Should always be two digits.
Minutes: Should omit leading zeros when they aren't needed. Use "0" if the duration is less than one minute.
Hours: Should be included only if they're greater than zero.
Tests:
format(500) should return "8:20".
format(4000) should return "1:06:40".
format(1) should return "0:01".
format(5555) should return "1:32:35".
format(99999) should return "27:46:39".