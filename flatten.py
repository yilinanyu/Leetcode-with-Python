def flatten(l):
    '''Flatten a arbitrarily nested lists and return the result as a single list.
    '''

    ret = []
    for i in l:
        if isinstance(i, list) or isinstance(i, tuple):
            ret.extend(flatten(i))
        else:
            ret.append(i)
    return ret
l = ['a', [1, 2], (3, 4, 5, [7, 8, ['gnu', 'linux']]), ['a', 'b', 'c'], [['d', 'e', 'f'], 12, [13, [14, [15,]]]]]
print flatten(l)