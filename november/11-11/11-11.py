def count(s):

    s = s.lower()
    vowels_count = 0
    consonants_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    

    for char in s:
        if char.isalpha():
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1

    print([vowels_count, consonants_count])

    return [vowels_count, consonants_count]

## Tests:
count("Hello World") #should return [3, 7].
count("JavaScript") #should return [3, 7].
count("Python") #should return [1, 5].
count("freeCodeCamp") #should return [5, 7].
count("Hello, World!") #should return [3, 7].
count("The quick brown fox jumps over the lazy dog.") #should return [11, 24].
