
Step1: Get the index of first (or leftmost) 1 in the first row.

Step2: Do following for every row after the first row
…IF the element on left of previous leftmost 1 is 0, ignore this row.
…ELSE Move left until a 0 is found. Update the leftmost index to this index and max_row_index to be the current row.

The time complexity is O(m+n) because we can possibly go as far left as we came ahead in the first step.

Following is C++ implementation of this method.

def leftmost1(matrix):
	#column 
	m = len(matrix[0])
	#row
	n = len(matrix)
	# get the first 1 in row 0
	j = binary_search(1,matrix[0])
	print j
	# no 1 in row 0
	if j == -1:
		j = 0
	for i in range(1,m):
		# move left when 1, 
		while j > 0 and matrix[i][j-1] == 1:
			j = j - 1
	return j
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
matrix = [
  [1, 1, 1, 1],
  [0, 0, 1, 1],
  [0, 0, 1, 1],
  [0, 0, 0, 0]]
print leftmost1(matrix)


