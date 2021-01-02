from abc import ABC
from enum import Enum


class Relation(Enum):
    SUBSET = 0
    SUPERSET = 0
    OVERLAPL = 0
    OVERLAPR = 0
    TOUCHINGL = 0
    TOUCHINGR = 0
    LESSDISJOINT = 0
    MOREDISJOINT = 0
    SAME = 0


class Range(ABC):
    def __init__(self, *args):
        if len(args) == 2:
            self.start = min(args[0], args[1])
            self.end = max(args[0], args[1])
        elif len(args) == 1:
            self.start = 0
            self.end = args[0]
        else:  # 0 args or more than 3 args
            self.start = self.end = 0

    def __reset__(self):
        self.start = self.end = 0

    def rStretch(self, *args):
        if len(args) == 0:
            self.end += 1
        else:
            self.end += args[0]

    def lStretch(self, *args):
        if len(args) == 0:
            self.start -= 1
        else:
            self.start -= args[0]

    def stretch(self, *args):
        if len(args) == 0:
            self.start -= 1
            self.end += 1
        else:
            self.start -= args[0]
            self.end += args[0]

    def squeeze(self, *args):
        if len(args) == 0:
            self.start += 1
            self.end -= 1
        else:
            self.start += args[0]
            self.end -= args[0]
        if self.start > self.end:
            self.__reset__()

    def shift(self, n: int = 1):
        self.start += n
        self.end += n

    def length(self) -> int:
        pass
        # return len(self.toList())

    def toString(self) -> str:
        pass

    def contains(self, x) -> bool:
        pass

    def equals(self, range_) -> bool:
        return self.start == range_.start and self.end == range_.end

    def isDisjoint(self, range_) -> bool:
        pass

    def isOverlapping(self, range_) -> bool:
        return not self.isDisjoint(range_)

    def lessThan(self, range_) -> bool:
        return self.length() < range_.length() if self.start == range_.start else self.start < range_.start

    def merge(self, range_):
        pass

    def common(self, range_):
        pass

    def classify(self, range_):
        if self.end == range_.start:
            return Relation.TOUCHINGR
        if (self.start == range_.end):
            return Relation.TOUCHINGL
        if (self.equals(range_)):
            return Relation.SAME
        if (self.contains(range_)):
            return Relation.SUPERSET
        if (range_.contains(self)):
            return Relation.SUBSET
        if (self.isDisjoint(range_)):
            if (self.start > range_.end):
                return Relation.MOREDISJOINT
            else:
                return Relation.LESSDISJOINT
        if (self.lessThan(range_)):
            return Relation.OVERLAPL
        return Relation.OVERLAPR

    def toList(self) -> [int]:
        pass


class OpenRange(Range):
    ''' (a, b) '''

    def toString(self) -> str:
        return f'({self.start}, {self.end})'

    def length(self) -> int:
        if self.end - self.start - 1 > 3:
            return self.end - self.start - 1
        return len(self.toList())

    def contains(self, x) -> bool:
        if isinstance(x, int):
            return self.start < x and x < self.end
        return self.start <= x.start and x.end <= self.end

    def isDisjoint(self, range_) -> bool:
        return (self.start - 1) >= (range_.end - 1) or (self.end - 1) <= (range_.start - 1)

    def merge(self, range_):
        if (self.isDisjoint(range_)):
            return OpenRange(0, 0)
        a = min(self.start, range_.start)
        b = max(self.end, range_.end)
        return OpenRange(a, b)

    def common(self, range_):
        if (self.isDisjoint(range_)):
            return OpenRange(0, 0)
        a, b = sorted([self.start, self.end, range_.start, range_.end])[1:3]
        return OpenRange(a, b)

    def toList(self) -> [int]:
        return list(range(self.start + 1, self.end))


class ClosedRange(Range):
    ''' [a, b] '''

    def toString(self) -> str:
        return f'[{self.start}, {self.end}]'

    def length(self) -> int:
        if self.end - self.start + 1 > 3:
            return self.end - self.start + 1
        return len(self.toList())

    def contains(self, x) -> bool:
        if isinstance(x, int):
            return self.start <= x and x <= self.end
        return self.start <= x.start and x.end <= self.end

    def isDisjoint(self, range_) -> bool:
        return self.start > range_.end or self.end < range_.start

    def merge(self, range_):
        if (self.isDisjoint(range_)):
            return ClosedRange(0, 0)
        a = min(self.start, range_.start)
        b = max(self.end, range_.end)
        return ClosedRange(a, b)

    def common(self, range_):
        if (self.isDisjoint(range_)):
            return ClosedRange(0, 0)
        a, b = sorted([self.start, self.end, range_.start, range_.end])[1:3]
        return ClosedRange(a, b)

    def toList(self) -> [int]:
        return list(range(self.start, self.end + 1))


class SemiOpenRange(Range):
    ''' [a, b) '''

    def toString(self) -> str:
        return f'[{self.start}, {self.end})'

    def length(self) -> int:
        if self.end - self.start > 3:
            return self.end - self.start
        return len(self.toList())

    def contains(self, x) -> bool:
        if isinstance(x, int):
            return self.start <= x and x < self.end
        return self.start <= x.start and x.end <= self.end

    def isDisjoint(self, range_) -> bool:
        return self.start > (range_.end - 1) or (self.end - 1) < range_.start

    def merge(self, range_):
        if (self.isDisjoint(range_)):
            return SemiOpenRange(0, 0)
        a = min(self.start, range_.start)
        b = max(self.end, range_.end)
        return SemiOpenRange(a, b)

    def common(self, range_):
        if (self.isDisjoint(range_)):
            return SemiOpenRange(0, 0)
        a, b = sorted([self.start, self.end, range_.start, range_.end])[1:3]
        return SemiOpenRange(a, b)

    def toList(self) -> [int]:
        return list(range(self.start, self.end))


range0 = ClosedRange(1, 3)
range1 = ClosedRange(3, 5)
range2 = OpenRange(3, 5)
range3 = SemiOpenRange(3, 5)

print(range1.toList())
print(range2.toList())
print(range3.toList())
print(range0.isOverlapping(range1))
print(range0.classify(range1))
print(range2.toString())
print(range3.toString())
