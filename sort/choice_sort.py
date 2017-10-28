from random import randint


def check_io(unsorted_list):
    length = len(unsorted_list)
    for i in range(length):
        for j in range(i + 1, length):
            if unsorted_list[j] < unsorted_list[i]:
                unsorted_list[i],  unsorted_list[j] = unsorted_list[j], unsorted_list[i]
    print(unsorted_list)
    return unsorted_list

if __name__ == '__main__':
    l = [ randint(0, 20) for _ in range(20)]
    print(l)
    s = sorted(l)
    assert check_io(l) == s, 'not sorted list!'
    