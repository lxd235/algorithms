"""
sort utils
"""
__all__ = ['exchange', 'less']


def exchange(target_list, index_a, index_b):
    target_list[index_a], target_list[index_b] = target_list[index_b], target_list[index_a]
    return None


def less(a, b):
    return a < b
