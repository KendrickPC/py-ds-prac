import string


def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    if isinstance(collection, list) == True:
        slicedList = collection[start:]
        return sought in slicedList
    if isinstance(collection, str) == True:
        return sought in collection
    if isinstance(collection, tuple) == True:
        slicedTuple = collection[start:]
        return sought in slicedTuple
    if isinstance(collection, set):
        return sought in collection
    if isinstance(collection, dict):
        return sought in collection.values()
    return "Please enter a valid data type for collection"

print(includes([1, 2, 3], 1))
print(includes([1, 2, 3], 1, 2))

print(includes("hello", "o"))
print(includes("hello", "z"))

print(includes(('Elmo', 5, 'red'), 'red', 1))
print(includes(('Elmo', 5, 'red'), 'blue', 1))

print(includes({1, 2, 3}, 1))
print(includes({1, 2, 3}, 1, 3))
print(includes({"apple": "red", "berry": "blue"}, "blue"))
