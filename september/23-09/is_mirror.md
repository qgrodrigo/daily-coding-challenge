String Mirror
Given two strings, determine if the second string is a mirror of the first.

A string is considered a mirror if it contains the same letters in reverse order.
Treat uppercase and lowercase letters as distinct.
Ignore all non-alphabetical characters.
Tests:
Passed:1. is_mirror("helloworld", "helloworld") should return False.
Passed:2. is_mirror("Hello World", "dlroW olleH") should return True.
Passed:3. is_mirror("RaceCar", "raCecaR") should return True.
Passed:4. is_mirror("RaceCar", "RaceCar") should return False.
Passed:5. is_mirror("Mirror", "rorrim") should return False.
Passed:6. is_mirror("Hello World", "dlroW-olleH") should return True.
Passed:7. is_mirror("Hello World", "!dlroW !olleH") should return True.