from binary_search import binary_search_iterative, binary_search_recursive
from linear_search import linear_search
import pytest

pytestmark = pytest.mark.parametrize("list, key", 
                        [([3,8,6,7,9,5,1,8,4], 0), 
                        ([3,8,6,7,9,5,1,8,4], 1), 
                        ([3,8,6,7,9,5,1,8,4], 2),
                        ([3,8,6,7,9,5,1,8,4], 3),
                        ([3,8,6,7,9,5,1,8,4], 4), 
                        ([3,8,6,7,9,5,1,8,4], 5), 
                        ([3,8,6,7,9,5,1,8,4], 6), 
                        ([3,8,6,7,9,5,1,8,4], 7), 
                        ([3,8,6,7,9,5,1,8,4], 8), 
                        ([3,8,6,7,9,5,1,8,4], 9),
                        ([3,8,6,7,9,5,1,8,4], 12),
                        ([3,8,6,7,9,5,1,8,4], -3),
                        ([1], 2),
                        ([3], 3)])

class TestBinarySearch:
    def test_recursive(self, list, key):
        list = sorted(list)
        if key in list:
            assert binary_search_recursive(0, len(list)-1, list, key) == list.index(key)
        else:
            assert binary_search_recursive(0, len(list)-1, list, key) == -1

    def test_iterative(self, list, key):
        list = sorted(list)
        if key in list:
            assert binary_search_iterative(list, key) == list.index(key)
        else:
            assert binary_search_iterative(list, key) == -1

class TestLinearSearch:
    def test_linear_search(self, list, key):
        if key in list:
            assert linear_search(list, key) == list.index(key)
        else:
            assert linear_search(list, key) == -1
         