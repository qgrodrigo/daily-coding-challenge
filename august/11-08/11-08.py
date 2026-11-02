def is_balanced(s):

    middle = 0

    if len(s) % 2 == 0:
        middle = int(len(s) / 2)
    else:
        middle = int(len(s) // 2 + 1)

    first_half = s[:middle-1]
    second_half = s[middle:]

    first_half_count = count_vowels(first_half)
    second_half_count = count_vowels(second_half)

    if first_half_count == second_half_count:
        print(True)
        return True
    else:
        print(False)
        return False

def count_vowels(word):
    count = 0
    word = word.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in word:
        if char in vowels:
            count += 1
    return count

#Tests:
is_balanced("racecar") #should return True.
is_balanced("Lorem Ipsum") #should return True.
is_balanced("Kitty Ipsum") #should return False.
is_balanced("string") #should return False.
is_balanced(" ") #should return True.
is_balanced("abcdefghijklmnopqrstuvwxyz") #should return False.
is_balanced("123A#b!E&*456-o.U") #should return True.
is_balanced("a") #should return True.
is_balanced("E") #should return True.