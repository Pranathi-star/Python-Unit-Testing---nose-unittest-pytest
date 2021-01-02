from interval import Range, ClosedRange, OpenRange, SemiOpenRange, Relation
import pytest


@pytest.mark.parametrize("rangeObj, expected_result", [
    (OpenRange(4), 3),
    (OpenRange(4, 4), 0),
    (OpenRange(4, 8), 3),
    (OpenRange(5, 4), 0),
    (OpenRange(0), 0),
    (OpenRange(), 0),
    (OpenRange(4, 5), 0),
    (ClosedRange(4), 5),
    (ClosedRange(4, 8), 5),
    (ClosedRange(4, 4), 1),
    (ClosedRange(0), 1),
    (ClosedRange(), 1),
    (ClosedRange(4, 5), 2),
    (SemiOpenRange(4), 4),
    (SemiOpenRange(4, 8), 4),
    (SemiOpenRange(4, 4), 0),
    (SemiOpenRange(5, 4), 1),
    (SemiOpenRange(0), 0),
    (SemiOpenRange(), 0),
    (SemiOpenRange(4, 5), 1)
])
def test_length(rangeObj, expected_result):
    assert rangeObj.length() == expected_result


@pytest.mark.parametrize("rangeObj, expected_result", [
    (OpenRange(4), [1, 2, 3]),
    (OpenRange(4, 4), []),
    (OpenRange(5, 4), []),
    (OpenRange(0), []),
    (OpenRange(), []),
    (OpenRange(4, 5), []),
    (ClosedRange(4), [0, 1, 2, 3, 4]),
    (ClosedRange(4, 4), [4]),
    (ClosedRange(0), [0]),
    (ClosedRange(), [0]),
    (ClosedRange(4, 5), [4, 5]),
    (SemiOpenRange(4), [0, 1, 2, 3]),
    (SemiOpenRange(4, 4), []),
    (SemiOpenRange(5, 4), [4]),
    (SemiOpenRange(0), []),
    (SemiOpenRange(), []),
    (SemiOpenRange(4, 5), [4])
])
def test_toList(rangeObj, expected_result):
    assert rangeObj.toList() == expected_result


@pytest.mark.parametrize("rangeObj, n, expected_result", [
    (OpenRange(4), 1, [2, 3, 4]),
    (OpenRange(4, 4), 2, []),
    (OpenRange(5, 4), 2, []),
    (OpenRange(0), 1, []),
    (OpenRange(), 1, []),
    (OpenRange(4, 5), 3, []),
    (ClosedRange(4), 1, [1, 2, 3, 4, 5]),
    (ClosedRange(4, 4), 2, [6]),
    (ClosedRange(0), 4, [4]),
    (ClosedRange(), 3, [3]),
    (ClosedRange(4, 5), 3, [7, 8]),
    (SemiOpenRange(4), 1, [1, 2, 3, 4]),
    (SemiOpenRange(4, 4), 5, []),
    (SemiOpenRange(5, 4), 3, [7]),
    (SemiOpenRange(0), 4, []),
    (SemiOpenRange(), 4, []),
    (SemiOpenRange(4, 5), 3, [7])
])
def test_shift(rangeObj, n, expected_result):
    rangeObj.shift(n)
    assert rangeObj.toList() == expected_result


@pytest.mark.parametrize("rangeObj, n, expected_result", [
    (OpenRange(4), 1, [0, 1, 2, 3, 4]),
    (OpenRange(0), 1, [0]),
    (OpenRange(4, 5), 1, [4, 5]),
    (ClosedRange(4), 1, [-1, 0, 1, 2, 3, 4, 5]),
    (ClosedRange(0), 1, [-1, 0, 1]),
    (ClosedRange(4, 5), 1, [3, 4, 5, 6]),
    (SemiOpenRange(4), 1, [- 1, 0, 1, 2, 3, 4]),
    (SemiOpenRange(0), 1, [-1, 0]),
    (SemiOpenRange(4, 5), 1, [3, 4, 5]),
    (OpenRange(4), 2, [-1, 0, 1, 2, 3, 4, 5]),
    (OpenRange(0), 3, [-2, -1, 0, 1, 2]),
    (OpenRange(4, 5), 2, [3, 4, 5, 6]),
    (ClosedRange(4), 3, [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]),
    (ClosedRange(0), 2, [-2, -1, 0, 1, 2]),
    (ClosedRange(4, 5), 3, [1, 2, 3, 4, 5, 6, 7, 8]),
    (SemiOpenRange(4), 2, [-2, -1, 0, 1, 2, 3, 4, 5]),
    (SemiOpenRange(0), 2, [-2, -1, 0, 1]),
    (SemiOpenRange(4, 5), 2, [2, 3, 4, 5, 6]),
])
def test_stretch(rangeObj, n, expected_result):
    rangeObj.stretch(n)
    assert rangeObj.toList() == expected_result


@pytest.mark.parametrize("rangeObj, n, expected_result", [
    (OpenRange(4), 1, [0, 1, 2, 3]),
    (OpenRange(0), 1, []),
    (OpenRange(4, 5), 1, [4]),
    (ClosedRange(4), 1, [-1, 0, 1, 2, 3, 4]),
    (ClosedRange(0), 1, [-1, 0]),
    (ClosedRange(4, 5), 1, [3, 4, 5]),
    (SemiOpenRange(4), 1, [- 1, 0, 1, 2, 3]),
    (SemiOpenRange(0), 1, [-1]),
    (SemiOpenRange(4, 5), 1, [3, 4]),
    (OpenRange(4), 2, [-1, 0, 1, 2, 3]),
    (OpenRange(0), 3, [-2, -1]),
    (OpenRange(4, 5), 2, [3, 4]),
    (ClosedRange(4), 3, [-3, -2, -1, 0, 1, 2, 3, 4]),
    (ClosedRange(0), 2, [-2, -1, 0]),
    (ClosedRange(4, 5), 3, [1, 2, 3, 4, 5]),
    (SemiOpenRange(4), 2, [-2, -1, 0, 1, 2, 3]),
    (SemiOpenRange(0), 2, [-2, -1]),
    (SemiOpenRange(4, 5), 2, [2, 3, 4]),
])
def test_lStretch(rangeObj, n, expected_result):
    rangeObj.lStretch(n)
    assert rangeObj.toList() == expected_result


@pytest.mark.parametrize("rangeObj, n, expected_result", [
    (OpenRange(4), 1, [1, 2, 3, 4]),
    (OpenRange(0), 1, []),
    (OpenRange(4, 5), 1, [5]),
    (ClosedRange(4), 1, [0, 1, 2, 3, 4, 5]),
    (ClosedRange(0), 1, [0, 1]),
    (ClosedRange(4, 5), 1, [4, 5, 6]),
    (SemiOpenRange(4), 1, [0, 1, 2, 3, 4]),
    (SemiOpenRange(0), 1, [0]),
    (SemiOpenRange(4, 5), 1, [4, 5]),
    (OpenRange(4), 2, [1, 2, 3, 4, 5]),
    (OpenRange(0), 3, [1, 2]),
    (OpenRange(4, 5), 2, [5, 6]),
    (ClosedRange(4), 3, [0, 1, 2, 3, 4, 5, 6, 7]),
    (ClosedRange(0), 2, [0, 1, 2]),
    (ClosedRange(4, 5), 3, [4, 5, 6, 7, 8]),
    (SemiOpenRange(4), 2, [0, 1, 2, 3, 4, 5]),
    (SemiOpenRange(0), 2, [0, 1]),
    (SemiOpenRange(4, 5), 2, [4, 5, 6]),
])
def test_rStretch(rangeObj, n, expected_result):
    rangeObj.rStretch(n)
    assert rangeObj.toList() == expected_result


@pytest.mark.parametrize("rangeObj, n, expected_result", [
    (OpenRange(4), 1, [2]),
    (OpenRange(0), 1, []),
    (OpenRange(4, 5), 1, []),
    (ClosedRange(4), 1, [1, 2, 3]),
    (ClosedRange(0), 1, [0]),
    (ClosedRange(4, 5), 1, [0]),
    (SemiOpenRange(4), 1, [1, 2]),
    (SemiOpenRange(0), 1, []),
    (SemiOpenRange(4, 5), 1, []),
    (OpenRange(4), 2, []),
    (OpenRange(0), 3, []),
    (OpenRange(4, 5), 1, []),
    (ClosedRange(4), 2, [2]),
    (ClosedRange(0), 2, [0]),
    (ClosedRange(4, 5), 3, [0]),
    (SemiOpenRange(4), 2, []),
    (SemiOpenRange(0), 2, []),
    (SemiOpenRange(4, 5), 2, []),
])
def test_squeeze(rangeObj, n, expected_result):
    rangeObj.squeeze(n)
    assert rangeObj.toList() == expected_result


@pytest.mark.parametrize("container, contained, expected_result", [
    (OpenRange(4), 4, False),
    (OpenRange(4), 0, False),
    (OpenRange(4), 3, True),
    (OpenRange(0), 0, False),
    (OpenRange(4),    OpenRange(0, 4), True),
    (OpenRange(5),    OpenRange(0, 4), True),
    (OpenRange(1, 4), OpenRange(3, 4), True),
    (OpenRange(0, 4), OpenRange(5), False),
    (OpenRange(1, 4), OpenRange(3, 5), False),
    (OpenRange(1, 2), OpenRange(4, 5), False),
    (OpenRange(4, 5), OpenRange(1, 2), False),
    (ClosedRange(4), 0, True),
    (ClosedRange(4), 4, True),
    (ClosedRange(0), 0, True),
    (ClosedRange(4),    ClosedRange(0, 4), True),
    (ClosedRange(5),    ClosedRange(0, 4), True),
    (ClosedRange(1, 4), ClosedRange(3, 4), True),
    (ClosedRange(0, 4), ClosedRange(5), False),
    (ClosedRange(1, 4), ClosedRange(3, 5), False),
    (ClosedRange(1, 2), ClosedRange(4, 5), False),
    (ClosedRange(4, 5), ClosedRange(1, 2), False),
    (SemiOpenRange(4),  4, False),
    (SemiOpenRange(4),  0, True),
    (SemiOpenRange(0),  0, False),
    (SemiOpenRange(4),    SemiOpenRange(0, 4), True),
    (SemiOpenRange(5),    SemiOpenRange(0, 4), True),
    (SemiOpenRange(1, 4), SemiOpenRange(3, 4), True),
    (SemiOpenRange(0, 4), SemiOpenRange(5), False),
    (SemiOpenRange(1, 4), SemiOpenRange(3, 5), False),
    (SemiOpenRange(1, 2), SemiOpenRange(4, 5), False),
    (SemiOpenRange(4, 5), SemiOpenRange(1, 2), False)
])
def test_contains(container, contained, expected_result):
    assert(container.contains(contained)) == expected_result


@pytest.mark.parametrize("rangeObj, testObj, expected_result", [
    (OpenRange(4, 5), OpenRange(4), True),
    (OpenRange(4, 5), OpenRange(5, 6), True),
    (SemiOpenRange(4), SemiOpenRange(6, 7), True),
    (SemiOpenRange(4), SemiOpenRange(4, 7), True),
    (SemiOpenRange(4, 7), SemiOpenRange(7, 8), True),
    (ClosedRange(4), ClosedRange(4, 6), False),
    (ClosedRange(4, 5), ClosedRange(3, 4), False),
    (ClosedRange(4), ClosedRange(4), False),
])
def test_isDisjoint(rangeObj, testObj, expected_result):
    assert(rangeObj.isDisjoint(testObj)) == expected_result


@pytest.mark.parametrize("rangeObj, testObj, expected_result", [
    (OpenRange(4, 5), OpenRange(4), []),
    (OpenRange(4, 6), OpenRange(3, 7), [5]),
    (SemiOpenRange(4), SemiOpenRange(6, 7), []),
    (SemiOpenRange(4, 6), SemiOpenRange(5), [4]),
    #(ClosedRange(3), ClosedRange(4, 5), []),
    (ClosedRange(4), ClosedRange(4), [0, 1, 2, 3, 4]),
])
def test_common(rangeObj, testObj, expected_result):
    assert (rangeObj.common(testObj)).toList() == expected_result


@pytest.mark.parametrize("rangeObj, testObj, expected_result", [
    (OpenRange(4, 5), OpenRange(4), []),
    (OpenRange(4, 6), OpenRange(3, 7), [4, 5, 6]),
    (SemiOpenRange(4), SemiOpenRange(6, 7), []),
    (SemiOpenRange(4, 6), SemiOpenRange(5), [0, 1, 2, 3, 4, 5]),
    #(ClosedRange(3), ClosedRange(4, 5), []),
    (ClosedRange(4), ClosedRange(4), [0, 1, 2, 3, 4]),
])
def test_merge(rangeObj, testObj, expected_result):
    assert (rangeObj.merge(testObj)).toList() == expected_result
