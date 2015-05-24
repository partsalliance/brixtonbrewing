from HotLiquidTank import HotLiquidTank

import unittest

class HotLiquidTank_tests(unittest.TestCase):
    def setUp(self):
        print "set up"
        HLT = HotLiquidTank()
    def test_heatItUp(self):
        HLT.heatTo(70)
        
        
if __name__ == '__main__':
    unittest.main()        
