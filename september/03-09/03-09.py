def is_pangram(sentence, letters):

    allowed = set(letters)
    found = set()

    for char in sentence.lower():
        if char.isalpha():
            if char not in allowed:
                print(False)
                return False
            found.add(char)
    print(found == allowed)
    return found == allowed

## Tests:
is_pangram("hello", "helo") #should return True
is_pangram("hello", "hel") #should return False
is_pangram("hello", "helow") #should return False
is_pangram("hello world", "helowrd") #should return True
is_pangram("Hello World!", "helowrd") #should return True
is_pangram("Hello World!", "heliowrd") #should return False
is_pangram("freeCodeCamp", "frcdmp") #should return False
is_pangram("The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz") #should return True