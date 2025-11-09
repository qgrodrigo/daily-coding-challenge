def spookify(boo):
    
    word = replace_undescord(boo)
    return capitalize(word)

def replace_undescord(word):

    new_word = ""
    for char in word:
        if(char == "-" or char == "_"):
            char = "~"
        new_word += char

    return new_word

def capitalize(word):

    fixed_word = ""
    count = 0

    for i in range(len(word)):
        
        if(word[i] != "~"):
            if(count % 2 == 0):
                fixed_word += word[i].upper()
                count += 1       
            else:
                fixed_word += word[i].lower()
                count += 1 
        else:
            fixed_word += word[i]

            if(count % 2 == 0):
                count = 0
            else:  
                count = 1
            
        
    return fixed_word
