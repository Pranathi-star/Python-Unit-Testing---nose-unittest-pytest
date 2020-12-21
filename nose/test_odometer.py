import odometer

class TestOdometer:
    def isAscending(self):
        assert odometer.Odometer.is_ascending(22) == False
        assert odometer.Odometer.is_ascending(312) == False
        assert odometer.Odometer.is_ascending(123) == True
        assert odometer.Odometer.is_ascending(90) == False

    def nextReading(self):
        assert odometer.Odometer.next_reading(89) == 12
        assert odometer.Odometer.next_reading(129) == 134

    def prevReading(self):
        assert odometer.Odometer.prev_reading(123) == 789
        assert odometer.Odometer.next_reading(23) == 19


