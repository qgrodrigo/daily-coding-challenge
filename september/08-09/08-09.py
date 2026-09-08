
def build_acronym(s):

    words = s.split()
    ignore_words = ['a', 'for', 'an', 'and', 'by', 'of']
    acronym = ''

    for i in range(len(words)):
            
        word = words[i]
            
        if(i == 0):
            acronym += word[0].upper()
        else:
            if word not in ignore_words:
                acronym += word[0].upper()
                
    return acronym

# test
#print (build_acronym("for your information"))
assert build_acronym("for your information") == "FYI"