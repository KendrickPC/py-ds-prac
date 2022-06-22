def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    results = []
    falsy = ['', [], False, (), None, 0]
    for item in lst:
        if item not in falsy:
            results.append(item)
    return results

print(compact([0, 1, 2, '', [], False, (), None, 'All done']))
