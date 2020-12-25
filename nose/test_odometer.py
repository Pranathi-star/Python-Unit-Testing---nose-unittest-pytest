from odometer import Odometer

class TestOdometer:
    def isAscending(self):
        assert Odometer(2).is_ascending(22) == False
        assert Odometer(3).is_ascending(312) == False
        assert Odometer(3).is_ascending(123) == True
        assert Odometer(2).is_ascending(90) == False

    def nextReading(self):
        assert Odometer(2).next_reading(89) == 12
        assert Odometer(3).next_reading(129) == 134

    def prevReading(self):
        assert Odometer(3).prev_reading(123) == 789
        assert Odometer(2).next_reading(23) == 19


