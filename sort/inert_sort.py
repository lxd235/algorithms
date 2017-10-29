from random import randint

from .sort_utils import *


def check_io(unsorted_list):
    length = len(unsorted_list)
    for i in range(length):
        t = i
        j = i - 1
        while j >= 0 and less(unsorted_list[t], unsorted_list[j]):
            exchange(unsorted_list, t, j)
            j -= 1
            t -= 1
    print(unsorted_list)
    return unsorted_list


if __name__ == '__main__':
    l = [randint(0, 20) for _ in range(20)]
    print(l)
    s = sorted(l)
    assert check_io(l) == s, 'not sorted list!'
