# start of main.py **
import unittest

def hex_to_decimal(hex):
    count = 0
    hex = hex[::-1]
    i = 0
    while(i < len(hex)):
        count += to_decimal(hex[i: i+1]) * (16 ** i)
        i += 1
    
    return count


def to_decimal(number):
    new_number = number
    if(number == "A"):
        new_number = "10"
    elif(number == "B"):
        new_number = "11"
    elif(number == "C"):
        new_number = "12"
    elif(number == "D"):
        new_number = "13"
    elif(number == "E"):
        new_number = "14"
    elif(number == "F"):
        new_number = "15"

    return int(new_number)

# end of main.py **

class Test(unittest.TestCase):
    
    def testToDecimal(self):
        #given
        number = "A"
        #when
        decimal = to_decimal(number)
        #then
        self.assertEqual(10, decimal)

    def testHex_to_decimal(self):
        #given
        hex = "2E"
        #when
        decimal = hex_to_decimal(hex)
        #then
        self.assertEqual(46, decimal)

if __name__ == '__main__':
    unittest.main()