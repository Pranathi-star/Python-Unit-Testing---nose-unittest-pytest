from range import Range
import pytest


@pytest.mark.parametrize("container, contained, expected_result", [
    (Range(4), Range(0, 4), True),
    (Range(5), Range(0, 4), True),
    (Range(1, 4), Range(3, 4), True),
    (Range(0, 4), Range(5), False),
    (Range(1, 4), Range(3, 5), False),
    (Range(1, 2), Range(4, 5), False),
    (Range(4, 5), Range(1, 2), False)])
def test_contains(container, contained, expected_result):
    assert(container.contains(contained)) == expected_result


@pytest.mark.parametrize("first_range, second_range, expected_result", [
    (Range(1, 3), Range(2, 3), True),
    (Range(2, 3), Range(1, 3), True),
    (Range(1, 5), Range(6, 7), False),
    (Range(6, 7), Range(1, 5), False)])
def test_overlapping(first_range, second_range, expected_result):
    assert(first_range.overlaps(second_range)) == expected_result


@pytest.mark.parametrize("first_range, second_range, expected_result", [
    (Range(1, 2), Range(3, 4), True),
    (Range(3, 4), Range(1, 2), True),
    (Range(1, 3), Range(2, 3), False),
    (Range(2, 3), Range(1, 3), False)])
def test_disjoint(first_range, second_range, expected_result):
    assert(first_range.disjoint(second_range)) == expected_result


@pytest.mark.parametrize("first_range, second_range, expected_result", [
    (Range(1, 2), Range(2, 7), False),
    (Range(2, 7), Range(1, 2), False),
    (Range(1, 5), Range(4, 7), False),
    (Range(1, 2), Range(4, 7), False),
    (Range(4, 7), Range(1, 2), False)])
def test_touching(first_range, second_range, expected_result):
    assert(first_range.is_touching(second_range)) == expected_result


@pytest.mark.parametrize("smaller, larger, expected_result", [
    (Range(1, 3), Range(3, 10), True),
    (Range(1), Range(2), True),
    (Range(4, 5), Range(1, 2), False),
    (Range(2), Range(1), False),
    (Range(1), Range(1), False),
    (Range(1, 4), Range(2, 5), True),
    (Range(2, 6), Range(1, 4), False)])
def test_less_than(smaller, larger, expected_result):
    assert smaller.is_less_than(larger) == expected_result

@pytest.mark.parametrize("larger, smaller, expected_result", [
    (Range(1, 3), Range(3, 10), False),
    (Range(1), Range(2), False),
    (Range(4, 5), Range(1, 2), True),
    (Range(2), Range(1), True),
    (Range(1), Range(1), False),
    (Range(1, 4), Range(2, 5), False),
    (Range(2, 6), Range(1, 4), True)])
def test_more_than(larger, smaller, expected_result):
    assert larger.is_more_than(smaller) == expected_result

@pytest.mark.parametrize("first_range, second_range, expected_result", [
    (Range(1, 3), Range(1, 2), False),
    (Range(1), Range(2), False),
    (Range(4, 5), Range(4, 5), True),
    (Range(1), Range(1), True),
    (Range(2, 3), Range(3, 4), False),
    (Range(2), Range(3, 4), False)])
def test_equal_to(first_range, second_range, expected_result):
    assert first_range.is_equal_to(second_range) == expected_result

@pytest.mark.parametrize("first_range, second_range, expected_result", [
    (Range(1, 3), Range(2, 3), Range(1, 3)),
    (Range(1, 5), Range(6, 10), Range(0)),
    (Range(1, 2), Range(3), Range(3)),
    (Range(1, 5), Range(2, 3), Range(1, 5)),
    (Range(1, 3), Range(2, 5), Range(1, 5)),
    (Range(6, 10), Range(1, 5), Range(0)),
    (Range(2, 5), Range(1, 3), Range(1, 5))])
def test_merge(first_range, second_range, expected_result):
    assert first_range.merge(second_range).is_equal_to(expected_result)

@pytest.mark.parametrize("first_range, expected_result", [
    (Range(4, 8), Range(5, 7)),
    (Range(2, 3), Range(0)),
    (Range(2, 4), Range(3, 3))])
def test_squeeze_default(first_range, expected_result):
    first_range.squeeze()
    assert first_range.is_equal_to(expected_result)

@pytest.mark.parametrize("first_range, step, expected_result", [
    (Range(6, 8), 3, Range(0)),
    (Range(3, 8), 2, Range(5, 6)),
    (Range(2, 5), 1, Range(3, 4))])
def test_squeeze(first_range, step, expected_result):
    first_range.squeeze(step)
    assert first_range.is_equal_to(expected_result)

@pytest.mark.parametrize("first_range, step, expected_result", [
    (Range(6, 8), 5, Range(1, 3)),
    (Range(2, 5), 0, Range(2, 5))])
def test_shift_left(first_range, step, expected_result):
    first_range.shift_left(step)
    assert first_range.is_equal_to(expected_result)

@pytest.mark.parametrize("first_range, step, expected_result", [
    (Range(1, 3), 5, Range(6, 8)),
    (Range(2, 5), 0, Range(2, 5))])
def test_shift_right(first_range, step, expected_result):
    first_range.shift_right(step)
    assert first_range.is_equal_to(expected_result)

@pytest.mark.parametrize("first_range, step, expected_result", [
    (Range(6, 8), 5, Range(1, 8)),
    (Range(2, 5), 0, Range(2, 5))])
def test_stretch_left(first_range, step, expected_result):
    first_range.stretch_left(step)
    assert first_range.is_equal_to(expected_result)

@pytest.mark.parametrize("first_range, expected_result", [
    (Range(6, 8), Range(5, 8)),
    (Range(2, 5), Range(1, 5))])
def test_stretch_left_default(first_range, expected_result):
    first_range.stretch_left()
    assert first_range.is_equal_to(expected_result)

@pytest.mark.parametrize("first_range, step, expected_result", [
    (Range(1, 3), 5, Range(1, 8)),
    (Range(2, 5), 0, Range(2, 5))])
def test_stretch_right(first_range, step, expected_result):
    first_range.stretch_right(step)
    assert first_range.is_equal_to(expected_result)

@pytest.mark.parametrize("first_range, expected_result", [
    (Range(1, 3), Range(1, 4)),
    (Range(5), Range(6))])
def test_stretch_right_default(first_range, expected_result):
    first_range.stretch_right()
    assert first_range.is_equal_to(expected_result)

@pytest.mark.parametrize("first_range, left_step, right_step, expected_result", [
    (Range(6, 8), 5, 4, Range(1, 12)),
    (Range(2, 5), 0, 2, Range(2, 7))])
def test_stretch(first_range, left_step, right_step, expected_result):
    first_range.stretch(left_step, right_step)
    assert first_range.is_equal_to(expected_result)

@pytest.mark.parametrize("first_range, left_step, expected_result", [
    (Range(6, 8), 5, Range(1, 9)),
    (Range(2, 5), 0, Range(2, 6))])
def test_stretch_default_right(first_range, left_step, expected_result):
    first_range.stretch(left_step)
    assert first_range.is_equal_to(expected_result)

@pytest.mark.parametrize("first_range, expected_result", [
    (Range(6, 8), Range(5, 9)),
    (Range(2, 5), Range(1, 6))])
def test_stretch_default(first_range, expected_result):
    first_range.stretch()
    assert first_range.is_equal_to(expected_result)
