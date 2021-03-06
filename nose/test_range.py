from parameterized import parameterized
from nose.tools import assert_equals
import nose
from range import Range


class TestRangeMethods() :

    @parameterized([(Range(4), Range(0, 4), True), 
                    (Range(5), Range(0, 4), True), 
                    (Range(1, 4), Range(3, 4), True), 
                    (Range(0, 4), Range(5), False), 
                    (Range(1, 4), Range(3, 5), False), 
                    (Range(1, 2), Range(4, 5), False), 
                    (Range(4, 5), Range(1, 2), False)])
    def test_contains(self, container, contained, expected_result):
        assert_equals(container.contains(contained), expected_result)


    @parameterized([(Range(1, 3), Range(2, 3), True), 
                    (Range(2, 3), Range(1, 3), True), 
                    (Range(1, 5), Range(6, 7), False), 
                    (Range(6, 7), Range(1, 5), False)])
    def test_overlapping(self, first_range, second_range, expected_result):
        assert_equals(first_range.overlaps(second_range), expected_result)


    @parameterized([(Range(1, 2), Range(3, 4), True), 
                    (Range(3, 4), Range(1, 2), True), 
                    (Range(1, 3), Range(2, 3), False), 
                    (Range(2, 3), Range(1, 3), False)])
    def test_disjoint(self, first_range, second_range, expected_result):
        assert_equals(first_range.disjoint(second_range), expected_result)


    @parameterized([(Range(1, 3), Range(2, 7), True), 
                    (Range(1, 7), Range(1, 2), True), 
                    (Range(1, 5), Range(4, 7), True), 
                    (Range(1, 2), Range(4, 7), False), 
                    (Range(4, 7), Range(1, 2), False)])
    def test_touching(self, first_range, second_range, expected_result):
        assert_equals(first_range.touching(second_range), expected_result)


    @parameterized([(Range(1, 3), Range(3, 10), True), 
                    (Range(1), Range(2), True), 
                    (Range(4, 5), Range(1, 2), False), 
                    (Range(2), Range(1), False), 
                    (Range(1), Range(1), False), 
                    (Range(1, 4), Range(2, 5), True), 
                    (Range(2, 6), Range(1, 4), False)])
    def test_less_than(self, smaller, larger, expected_result):
        assert_equals(smaller.less_than(larger), expected_result)
        

if __name__ == "__main__" :
    nose.main()