# Longest Word
Given a sentence string, return the longest word in the sentence.

Words are separated by a single space.
Only letters (a-z, case-insensitive) count toward the word's length.
If there are multiple words with the same length, return the first one that appears.
Return the word as it appears in the given string, with punctuation removed.

## Tests:
longest_word("The quick red fox") should return "quick".
longest_word("Hello coding challenge.") should return "challenge".
longest_word("Do Try This At Home.") should return "This".
longest_word("This sentence... has commas, ellipses, and an exclamation point!") should return "exclamation".
longest_word("A tie? No way!") should return "tie".
longest_word("Wouldn't you like to know.") should return "Wouldnt".