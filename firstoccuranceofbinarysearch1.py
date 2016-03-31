def binary_search(x, a):
    # lon N 
    lo = 0
    hi = len(a)

    while lo < hi:
        mid = lo + (hi- lo) / 2

        if a[mid] < x:
            lo = mid + 1
        elif a[mid] > x:
            hi = mid 
        elif mid > 0 and a[mid-1] == x:
            hi = mid
        else:
            return mid

    return -1
print binary_search(2,[1,2,2,2,3])
