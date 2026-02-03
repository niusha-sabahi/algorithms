from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from quick_sort import quick_sort
import pytest

pytestmark = pytest.mark.parametrize("list", 
                                     [[3,8,2,7,5], 
                                      [3,8,2,7],
                                      [12,11,13,5,6],
                                      [5,7,8,3,7,7,2],
                                      [1,2,3,4,5,6],
                                      [78,94,62,6,2,0,7,67],
                                      [2536,67,3,89,2,9,56,784],
                                      [-5,-8,-3,-45,-12,-12],
                                      [6,8,3,0,4,25,0],
                                      [-5,8,3,0,-6,-4,1,1],
                                      [1],
                                      []])

class TestSorting:
    def test_bubble_sort(self, list):
        assert bubble_sort(list) == sorted(list)
    
    def test_insertion_sort(self, list):
        assert insertion_sort(list) == sorted(list)

    def test_selection_sort(self, list):
        assert selection_sort(list) == sorted(list)

    def test_quick_sort(self, list):
        assert quick_sort(list) == sorted(list)

        