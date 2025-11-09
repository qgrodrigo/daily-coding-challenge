def verify(message, key, signature):

    message_value = total_value(message)
    key_value = total_value(key)
    signature_value = False

    if(sum_value(message_value,key_value) == signature):
        signature_value = True

    return signature_value

def sum_value(message, key):
    return message + key

def total_value(message):
    sum_char_value = 0
    
    for char in message:
        sum_char_value += value_to_char(char)
    
    return sum_char_value

def value_to_char(char):

    if 'a' <= char <= 'z':
        return ord(char) - ord('a') + 1
    elif 'A' <= char <= 'Z':
        return ord(char) - ord('A') + 27
    else:
        return 0
