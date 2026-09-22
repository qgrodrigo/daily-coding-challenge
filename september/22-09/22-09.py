def digits_or_letters(s):

    count_letters = 0
    count_digits = 0
    message = ''

    #clean alphanumerics
    clean_word = ''.join(filter(str.isalnum, s))

    #count only letters or digits
    for letter in clean_word:
        if(letter.isalpha()):
            count_letters +=1
        else:
            count_digits += 1

    #compare
    if(count_letters > count_digits):
        message = 'letters'
    elif(count_digits > count_letters):
        message = 'digits'
    else:
        message = 'tie'

    print(message)


    return message

digits_or_letters("abc123") #should return "tie".
digits_or_letters("a1b2c3d") #should return "letters".
digits_or_letters("1a2b3c4") #should return "digits".
digits_or_letters("abc123!@#DEF") #should return "letters".
digits_or_letters("H3110 W0R1D") #should return "digits".
digits_or_letters("P455W0RD") #should return "tie".