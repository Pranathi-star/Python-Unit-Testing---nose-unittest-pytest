class Range:

    def __init__(self, *args):
        """
        Sets starts to 0 if only one argument provided else
        sets start and end according to the arguments passed.
        """
        if(len(args) < 1 or len(args) > 2):
            raise ValueError
        self.start = 0 if len(args) == 1 else args[0]
        self.end = args[0] if len(args) == 1 else args[1]
        return

    def __repr__(self):
        return f"[{self.start}, {self.end})"

    def __len__(self):
        return self.end - self.start

    def contains(self, sub) -> bool:
        """
        If the starting and ends point of the sub range are
        within the super range, it returns True 
        """
        return self.start <= sub.start and self.end >= sub.end

    def disjoint(self, sub) -> bool:
        """
        If two ranges don't overlap, then they are disjoint.
        """
        return sub.start > self.end or self.start > sub.end

    def overlaps(self, sub) -> bool:
        """
        Finds the smaller of the two starting points and checks if
        the end point of the one that started eariler finishes before
        or after the range that started after.
        """
        return not self.disjoint(sub)

    def is_touching(self, sub) -> bool:
        """
        Finds the smaller of the two starting points and checks if
        the end point of the one that started eariler is equal to
        the starting point of the range that started after.
        """
        return sub.start == self.end if self.start < sub.start else self.start == sub.end

    def is_less_than(self, sub) -> bool:
        """
        If both start points are equal, returns True if the super range 
        ends before the sub range else returns True if the super range
        """
        return self.end < sub.end if self.start == sub.start else self.start < sub.start

    def is_more_than(self, sub) -> bool:
        """
        If both start points are equal, returns True if the super range ends before the sub range
        """
        return self.end > sub.end if self.start == sub.start else self.start > sub.start

    def is_equal_to(self, sub) -> bool:
        """
        Returns True if the starting and ending points of both
        ranges are the same.
        """
        return self.start == sub.start and self.end == sub.end

    def stretch_left(self, left=1):
        self.start -= left

    def stretch_right(self, right=1):
        self.end += right

    def stretch(self, left=1, right=1):
        self.start -= left
        self.end += right

    def squeeze(self, n=1):
        pass

    def shift(self, n):
        pass

    def shift_left(self, n):
        pass

    def shift_right(self, n):
        pass

    def classify(self):
        pass

    def merge(self, sub):
        if self.disjoint(sub):
            return Range(0)
        else:
            return Range(min(self.start, sub.start), max(self.end, sub.end))

    def common(self):
        pass


if __name__ == "__main__":
    a = Range(8)
    b = Range(4, 9)
    print(a)
    print(b)
    print(a.contains(b))
    print(b.contains(a))
    print(a.overlaps(b))
    print(b.overlaps(a))
    print(a.disjoint(b))
    print(b.disjoint(a))
    print(a.is_touching(b))
    print(b.is_less_than(a))
