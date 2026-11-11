# Pangram
Given a word or sentence and a string of lowercase letters, determine if the word or sentence uses all the letters from the given set at least once and no other letters.

Ignore non-alphabetical characters in the word or sentence.
Ignore letter casing in the word or sentence.

## Tests:
is_pangram("hello", "helo") should return True
is_pangram("hello", "hel") should return False
is_pangram("hello", "helow") should return False
is_pangram("hello world", "helowrd") should return True
is_pangram("Hello World!", "helowrd") should return True
is_pangram("Hello World!", "heliowrd") should return False
is_pangram("freeCodeCamp", "frcdmp") should return False
is_pangram("The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz") should return True