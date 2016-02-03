def findUpperBound(array, l, r, target):
        while l < r:
                mid = l + (r - l) / 2
                if array[mid] > target:
                        r = mid
                else:
                        l = mid + 1
        return l