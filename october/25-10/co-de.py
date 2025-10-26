
def complementary_dna(strand):

    DICTIONARY = {
        "A" : "T",
        "T" : "A",
        "C" : "G",
        "G" : "C"
    }

    complementary = ""
    for char in strand:
        complementary += DICTIONARY[char]
    
    return complementary

