def bsearch(array, l, r, target):
	while l <= r:
		mid = l + （r - l)/2
		if array[mid] > target:
			r = mid - 1
		elif array[mid] < target:
			l = mid + 1
		else:
			return l
	return -1
