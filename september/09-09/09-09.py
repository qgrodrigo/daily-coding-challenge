def all_unique(s):

    is_unique = True

    
    for i in range(len(s)-2):
        
        cut = s[i+1 : len(s)]

        if s[i] in cut:
            is_unique = False

        
    print(is_unique)    
              
    return is_unique

all_unique("!@#*$%^&*()aA")
