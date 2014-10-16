from HeatElement import HeatElement
import unittest

class HeatElement_tests(unittest.TestCase):
    
    def setUp(self):
        h = HeatElement(12,14)
        print " setup"
    def test_notRunning(self):
        h = HeatElement(12,14)
        self.assertFalse(h.running)

    def test_switchElementOn(self):
        h = HeatElement(12,14)
        self.assertFalse(h.running)
        h.turnElementOn()
        self.assertTrue(h.running)

    def test_elementIsAlreadyOn(self):
        h = HeatElement(12,14)
        self.assertFalse(h.running)
        h.running = True
        self.assertTrue(h.running)
        self.assertEqual(h.turnElementOn(),"element already on")

    def test_switchElementOff(self):
        h = HeatElement(12,14)
        h.running = True
        self.assertTrue(h.running)
        h.turnElementOff()
        self.assertFalse(h.running)

    def test_elementIsAlreadyOff(self):
        h = HeatElement(12,14)
        self.assertEqual(h.turnElementOff(),"element already off")
        
if __name__ == '__main__':
    unittest.main()
    
