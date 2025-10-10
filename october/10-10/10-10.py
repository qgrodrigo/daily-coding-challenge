import unittest

def launch_fuel(payload):
    count = 0
    while(payload > 1):
        payload = payload / 5
        count += payload
        #print(masa)
    return round(count,1)

class test(unittest.TestCase):
    '''
    1. launchFuel(50) should return 12.4.
    2. launchFuel(500) should return 124.8.
    3. launchFuel(243) should return 60.7.
    4. launchFuel(11000) should return 2749.8.
    5. launchFuel(6214) should return 1553.4.
    '''
    def test_launch_fuel(self):
        result_one = launch_fuel(50)
        self.assertEqual(12.4, result_one)
        
        result_two = launch_fuel(500)
        self.assertEqual(124.8, result_two)
        
        result_trhee = launch_fuel(243)
        self.assertEqual(60.7, result_trhee)
        
        result_trhee = launch_fuel(11000)
        self.assertEqual(2749.8, result_trhee)
        
        result_trhee = launch_fuel(6214)
        self.assertEqual(1553.4, result_trhee)
    
if __name__ == '__main__':
    unittest.main()
