import unittest
import odometer

class TestOdometer(unittest.TestCase):
    def test_ascending(self):
        self.assertEqual(odometer.Odometer.is_ascending(11), False)
        self.assertEqual(odometer.Odometer.is_ascending(-123), True)
        self.assertEqual(odometer.Odometer.is_ascending(2), True)
        self.assertEqual(odometer.Odometer.is_ascending(123456789), True)
        self.assertEqual(odometer.Odometer.is_ascending(12.34), True)
    
    def test_next_reading(self, step = 1):
        pass
    def test_prev_reading(self, step = 1):
        pass
    def test_diff(self, o = 1):
        pass

if __name__ == '__main__':
    unittest.main()
