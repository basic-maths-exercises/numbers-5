import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_function(self) :
        for b in range(2,11) :
            for i in range(20) :
                val = np.random.randint(0,127)
                arr = convertToBase(val,b) 
                for j in range(7) : 
                    ppp = b**(6-j)
                    vv = int(np.floor( val / ppp ) )
                    val = val - vv*ppp
                    self.assertTrue( vv==arr[6-j], "Your function is not working" )
