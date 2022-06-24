# import pytest
from xmin import get_list, main, set_list

l1_list = [[2, 4, 3], [0], [9, 9, 9, 9, 9, 9, 9]]
l2_list = [[5, 6, 4], [0], [9, 9, 9, 9]]
expected_list = [[7, 0, 8], [0], [8, 9, 9, 9, 0, 0, 0, 1]]


def test():
    for l1, l2, expected in zip(l1_list, l2_list, expected_list):
        l1 = set_list(l1)
        l2 = set_list(l2)
        expected.reverse()
        expected = set_list(expected)

        xs = main(l1, l2)
        assert xs == expected
        print(xs)
        print(expected)
        print(expected == xs)


test()
