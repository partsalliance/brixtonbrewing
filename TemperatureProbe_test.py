from TemperatureProbe import TemperatureProbe
import unittest

class TemperatureProbe_tests(unittest.TestCase):

        def setUp(self):
            print "set up"

        def test_checkForReading(self):
            t = TemperatureProbe()
            print t.read_temp_raw()
if __name__ == '__main__':
    unittest.main()
