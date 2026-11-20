def one_hundred(chars):

    sentence = chars * (100 // len(chars) + 1)

    only_one_hundred_sentence = sentence[0:100]

    print(len(only_one_hundred_sentence))
    return only_one_hundred_sentence

## Tests:
one_hundred("One hundred ") #should return "One hundred One hundred One hundred One hundred One hundred One hundred One hundred One hundred One ".
one_hundred("freeCodeCamp ") #should return "freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeC".
one_hundred("daily challenges ") #should return "daily challenges daily challenges daily challenges daily challenges daily challenges daily challenge".
one_hundred("!") #should return "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!".