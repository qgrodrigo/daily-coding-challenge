Acronym Builder
Given a string containing one or more words, return an acronym of the words using the following constraints:

The acronym should consist of the first letter of each word capitalized, unless otherwise noted.
The acronym should ignore the first letter of these words unless they are the first word of the given string: a, for, an, and, by, and of.
The acronym letters should be returned in the order they are given.
The acronym should not contain any spaces.
Tests:
Passed:1. buildAcronym("Search Engine Optimization") should return "SEO".
Passed:2. buildAcronym("Frequently Asked Questions") should return "FAQ".
Passed:3. buildAcronym("National Aeronautics and Space Administration") should return "NASA".
Passed:4. buildAcronym("Federal Bureau of Investigation") should return "FBI".
Passed:5. buildAcronym("For your information") should return "FYI".
Passed:6. buildAcronym("By the way") should return "BTW".
Passed:7. buildAcronym("An unstoppable herd of waddling penguins overtakes the icy mountains and sings happily") should return "AUHWPOTIMSH".