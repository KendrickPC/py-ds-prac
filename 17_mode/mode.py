# https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/

def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    dict = {}
    count, itm = 0, ''
    for item in reversed(nums):
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count:
            count, itm = dict[item], item
    return (itm)

print(mode([1, 2, 1]))
print(mode([2, 2, 3, 3, 2]))
