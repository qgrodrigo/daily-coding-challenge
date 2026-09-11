def reverse_sentence(sentence):
    
    words = sentence.split()
    words.reverse()
    reverse = ' '.join(words)

    print(reverse)

    



    return reverse

reverse_sentence("world hello") #should return "hello world".