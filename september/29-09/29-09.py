def get_longest_word(sentence):

    sentence = sentence.replace('.', '')
    sentence = sentence.split()

    long_word = max(sentence, key=len)


    return long_word


#Tests:
get_longest_word("coding is fun") #should return "coding".
get_longest_word("Coding challenges are fun and educational.") #should return "educational".
get_longest_word("This sentence has multiple long words.") #should return "sentence".