from interval import Range, ClosedRange, OpenRange, SemiOpenRange, Relation
import pytest

# OpenRange
@pytest.mark.parametrize("container, contained, expected_result", [
    (OpenRange(4), 3, True),
    (OpenRange(4),    OpenRange(0, 4), True),
    (OpenRange(5),    OpenRange(0, 4), True),
    (OpenRange(1, 4), OpenRange(3, 4), True),
    (OpenRange(0, 4), OpenRange(5), False),
    (OpenRange(1, 4), OpenRange(3, 5), False),
    (OpenRange(1, 2), OpenRange(4, 5), False),
    (OpenRange(4, 5), OpenRange(1, 2), False)])
def test_contains_OpenRange(container, contained, expected_result):
    assert(container.contains(contained)) == expected_result


# ClosedRange
@pytest.mark.parametrize("container, contained, expected_result", [
    (ClosedRange(4),    ClosedRange(0, 4), True),
    (ClosedRange(5),    ClosedRange(0, 4), True),
    (ClosedRange(1, 4), ClosedRange(3, 4), True),
    (ClosedRange(0, 4), ClosedRange(5), False),
    (ClosedRange(1, 4), ClosedRange(3, 5), False),
    (ClosedRange(1, 2), ClosedRange(4, 5), False),
    (ClosedRange(4, 5), ClosedRange(1, 2), False)])
def test_contains_ClosedRange(container, contained, expected_result):
    assert(container.contains(contained)) == expected_result

# SemiOpenRange
@pytest.mark.parametrize("container, contained, expected_result", [
    (SemiOpenRange(4),    SemiOpenRange(0, 4), True),
    (SemiOpenRange(5),    SemiOpenRange(0, 4), True),
    (SemiOpenRange(1, 4), SemiOpenRange(3, 4), True),
    (SemiOpenRange(0, 4), SemiOpenRange(5), False),
    (SemiOpenRange(1, 4), SemiOpenRange(3, 5), False),
    (SemiOpenRange(1, 2), SemiOpenRange(4, 5), False),
    (SemiOpenRange(4, 5), SemiOpenRange(1, 2), False)])
def test_contains_SemiOpenRange(container, contained, expected_result):
    assert(container.contains(contained)) == expected_result
