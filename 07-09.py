def parse_roman_numeral(numeral):
    
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    
    suma = 0
    
    for i in range(len(numeral)-1):
        if(romans[numeral[i]] < romans[numeral[i+1]]):
            suma -= romans[numeral[i]]
        else:
            suma += romans[numeral[i]]
    
    suma += romans[numeral[len(numeral)-1]]
    
    #print(suma)
    return suma