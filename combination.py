
# itertools.product should do the trick.

>>> list(itertools.product([1, 5, 8], [0.5, 4]))
[(1, 0.5), (1, 4), (5, 0.5), (5, 4), (8, 0.5), (8, 4)]