from odometer import Odometer
import pytest


@pytest.mark.parametrize("odometer, num, expected_result", [
    (Odometer(1), 1, True),
    (Odometer(2), 19, True),
    (Odometer(2), 90, False),
    (Odometer(3), 123, True),
    (Odometer(3), 543, False),
    (Odometer(3), 560, False),
])
def test_is_ascending(odometer, num, expected_result):
    assert odometer.is_ascending(num) == expected_result


@pytest.mark.parametrize("odometer, step, expected_result", [
    (Odometer(1), 0, 1),
    (Odometer(1), 1, 2),
    (Odometer(1), 9, 1),
    (Odometer(2), 4, 16),
    (Odometer(2), 35, 89),
    (Odometer(2), 36, 12),
    (Odometer(2), 1, 13),
    (Odometer(3), 1, 124),
    (Odometer(3), 84, 123),
])
def test_next_reading(odometer, step, expected_result):
    odometer.next_reading(step)
    assert odometer.get_position() == expected_result


def test_previous_reading():
    pass


def test_diff():
    pass
