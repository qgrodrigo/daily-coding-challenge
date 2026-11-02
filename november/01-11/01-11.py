def verify(message, key, signature):

    message_sum = 0
    key_sum = 0
    is_matched = True

    for char in message:
        message_sum += letter_value(char)

    for char in key:
        key_sum += letter_value(char)

    if message_sum + key_sum != signature:
        is_matched = False

    print(is_matched)

    return is_matched

def letter_value(letter: str) -> int:
    value = 0
    if letter.islower():
        value = ord(letter) - 96
    if letter.isupper():
        value = ord(letter) - 38
    
    return value
## Tests:
verify("foo", "bar", 57) #should return True.
verify("foo", "bar", 54) #should return False.
verify("freeCodeCamp", "Rocks", 238) #should return True.
verify("Is this valid?", "No", 210) #should return False.
verify("Is this valid?", "Yes", 233) #should return True.
verify("Check out the freeCodeCamp podcast,", "in the mobile app", 514) #should return True.