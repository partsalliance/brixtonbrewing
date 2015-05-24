from TemperatureProbe import TemperatureProbe
import unittest
import time

class TemperatureProbe_tests(unittest.TestCase):

        def setUp(self):
            print "set up"

        def test_checkForReading(self):
            t = TemperatureProbe()
            print(t.read_temp())
            self.assertGreater(t.read_temp(),0)

        def test_startLogging(self):
            t = TemperatureProbe()
            print(t.read_temp())
            t.activateLogging()
            self.assertTrue(t.activeLogging)
            time.sleep(15)
            print ("other loop")
            time.sleep(3)
            t.deactivateLogging()
            self.assertFalse(t.activeLogging)
if __name__ == '__main__':
    unittest.main()
