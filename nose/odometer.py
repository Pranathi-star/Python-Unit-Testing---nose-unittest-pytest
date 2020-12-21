class Odometer:
    @staticmethod
    def is_ascending(n: int) -> bool:
        if n < 10:
            return True
        if n % 10 <= (n // 10) % 10:
            return False
        return Odometer.is_ascending(n // 10)

    def __init__(self, size):
        self.readings = []
        if size not in range(2, 9):
            self.size = 0
            return 
        for n in range(10 ** (size - 1), 10 ** size):
            if Odometer.is_ascending(n):
                self.readings.append(n)
        self.SIZE = size
        self.LENGTH = len(self.readings)
        self.position = 0
        return

    def __DEBUG__(self):
        print(f"Size = {self.SIZE}, First = {self.readings[0]}", end = " ")
        print(f"Last = {self.readings[-1]}", end = " ")
        print(f"Current = {self.readings[self.position]}", end = " ")
        print(f"Position = {self.position}")

    def next_reading(self, step = 1):
        self.position += step
        self.position %= self.LENGTH
        return self.readings[self.position]

    def prev_reading(self, step = 1):
        self.position -= step
        self.position %= self.LENGTH
        return self.readings[self.position]

    def diff(self, o):
        if self.SIZE != o.SIZE:
            return -1
        togo = o.position - self.position
        if togo < 0:
            togo += self.LENGTH
        return togo

o = Odometer(3)
p = Odometer(2)
print(o.next_reading(3))
o.__DEBUG__()

