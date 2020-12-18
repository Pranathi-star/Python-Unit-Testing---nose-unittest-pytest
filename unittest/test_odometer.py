import unittest
import odometer

class TestOdometer(unittest.TestCase):
    def test_ascending(self):
        result = odometer.Odometer.is_ascending(11)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
