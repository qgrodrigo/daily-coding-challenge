Array Diff
Given two arrays with strings values, return a new array containing all the values that appear in only one of the arrays.

The returned array should be sorted in alphabetical order.
Tests:
Waiting:1. array_diff(["apple", "banana"], ["apple", "banana", "cherry"]) should return ["cherry"].
Waiting:2. array_diff(["apple", "banana", "cherry"], ["apple", "banana"]) should return ["cherry"].
Waiting:3. array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"]) should return ["eight", "four", "six", "two"].
Waiting:4. array_diff(["two", "four", "five", "eight"], ["one", "two", "three", "four", "seven", "eight"]) should return ["five", "one", "seven", "three"].
Waiting:5. array_diff(["I", "like", "freeCodeCamp"], ["I", "like", "rocks"]) should return ["freeCodeCamp", "rocks"].