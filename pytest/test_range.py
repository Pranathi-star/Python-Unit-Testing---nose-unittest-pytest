from range import Range
import pytest


@pytest.mark.parametrize("container, contained", [(Range(4), Range(0, 4)), (Range(5), Range(0, 4)), (Range(1, 4), Range(3, 4))])
def test_contains(container, contained):
    assert(container.contains(contained)) == True


@pytest.mark.parametrize("container, contained", [(Range(0, 4), Range(5)), (Range(1, 4), Range(3, 5)), (Range(1, 2), Range(4, 5)), (Range(4, 5), Range(1, 2))])
def test_does_not_contain(container, contained):
    assert(container.contains(contained)) == False


def test_overlaps():
    pass


def test_disjoint():
    pass


def test_touching():
    pass


@pytest.mark.parametrize("smaller, larger", [(Range(1, 2), Range(3, 10)), (Range(1), Range(2))])
def test_less_than(smaller, larger):
    assert smaller.less_than(larger) == True


@pytest.mark.parametrize("smaller, larger", [(Range(2), Range(1)), (Range(1), Range(1)), (Range(1, 4), Range(2, 5)), (Range(2, 6), Range(1, 4))])
def test_not_less_than(smaller, larger):
    assert smaller.less_than(larger) == False
