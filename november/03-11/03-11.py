def count_words(sentence):

    words = sentence.split()
    count = len(words)    

    print(count)

    return count

#Tests:
count_words("Hello world") #should return 2.
count_words("The quick brown fox jumps over the lazy dog.") #should return 9.
count_words("I like coding challenges!") #should return 4.
count_words("Complete the challenge in JavaScript and Python.") #should return 7.
count_words("The missing semi-colon crashed the entire internet.") #should return 7.