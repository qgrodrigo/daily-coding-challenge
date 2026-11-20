def longest_word(sentence):

    longest = ''

    for word in sentence.split():
        clean = ''.join(ch for ch in word if ch.isalpha())
        if len(clean) > len(longest):
            longest = clean

    print(longest)
    return longest
## Tests:
longest_word("The quick red fox") #should return "quick".
longest_word("Hello coding challenge.") #should return "challenge".
longest_word("Do Try This At Home.") #should return "This".
longest_word("This sentence... has commas, ellipses, and an exclamation point!") #should return "exclamation".
longest_word("A tie? No way!") #should return "tie".
longest_word("Wouldn't you like to know.") #should return "Wouldnt".