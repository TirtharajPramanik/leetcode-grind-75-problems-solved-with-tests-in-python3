import pytest
from main import get_result

nums_list = [[2, 7, 11, 15], [3, 2, 4], [3, 3], [1, 2, 3, 3], [1, 2, 3, 3]]
target_list = [9, 6, 6, 5, 6]
expected_list = [[0, 1], [1, 2], [0, 1], [1, 2], [2, 3]]


def test():
    for nums, target, expected in zip(nums_list, target_list, expected_list):
        x, y = get_result(nums, target)
        print('result:', [x, y])
        print('expected:', expected)
        print('_'*10)
        assert [x, y] == expected


test()
