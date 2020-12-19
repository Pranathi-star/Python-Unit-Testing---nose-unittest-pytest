class Range:

    def __init__(self, *args):
        """
        Sets starts to 0 if only one argument provided else
        sets start and end according to the arguments passed.
        """
        self.start = 0 if len(args) == 1 else args[0]
        self.end = args[0] if len(args) == 1 else args[1]
        return

    def __DEBUG__(self):
        print(f"Start = {self.start}, End = {self.end}")
        return

    def contains(self, sub) -> bool:
        """
        If the starting and ends point of the sub range are
        within the super range, it returns True 
        """
        return self.start <= sub.start and self.end >= sub.end

    def overlaps(self, sub) -> bool:
        """
        Finds the smaller of the two starting points and checks if
        the end point of the one that started eariler finishes before
        or after the range that started after.
        """
        return sub.start < self.end if self.start < sub.start else self.start < sub.end

    def disjoint(self, sub) -> bool:
        """
        If two ranges don't overlap, then they are disjoint.
        """
        return not self.overlaps(sub)

    def touching(self, sub) -> bool:
        """
        Finds the smaller of the two starting points and checks if
        the end point of the one that started eariler is equal to
        the starting point of the range that started after.
        """
        return sub.start == self.end if self.start < sub.start else self.start == sub.end

    def less_than(self, sub) -> bool:
        """
        Returns True if the length of the super range is
        less than the length of the sub range
        """
        return self.end - self.start < sub.end - sub.start


if __name__ == "__main__":
    a = Range(8)
    b = Range(4, 9)
    a.__DEBUG__()
    b.__DEBUG__()
    print(a.contains(b))
    print(b.contains(a))
    print(a.overlaps(b))
    print(b.overlaps(a))
    print(a.disjoint(b))
    print(b.disjoint(a))
    print(a.touching(b))
    print(b.less_than(a))
