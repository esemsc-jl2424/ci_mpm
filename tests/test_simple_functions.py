import pytest
import math
from simple_functions import my_sum, factorial, sinf


class TestSimpleFunctions(object):
    '''Class to test our simple functions are working correctly'''

    @pytest.mark.parametrize('iterable, expected', [
        ([8, 7, 5], 20),
        ((10, -2, 5, -10, 1), 4)
    ])
    def test_my_add(self, iterable, expected):
        '''Test our add function'''
        isum = my_sum(iterable)
        assert isum == expected

    @pytest.mark.parametrize('num, expected', [
        (5, 120),      # factorial(5) = 120
        (3, 6),        # factorial(3) = 6
        (0, 1),        # factorial(0) = 1
    ])
    def test_factorial(self, num, expected):
        '''Test our factorial function'''
        answer = factorial(num)
        assert answer == expected

    @pytest.mark.parametrize('angle, expected', [
        (0, 0),
        (math.pi / 2, 1),
        (3 * math.pi / 2, -1)])
    def test_sinf(self, angle, expected):
        '''Test our sin function'''
        answer = sinf(angle)
        assert answer == expected
