# Search Insert position of a target in the sorted arry
def search(self, A, target):
	left = 0; right = len(A)-1
	while left<= right:
		mid = (left + right)/2
		if A[mid]< target:
			left = mid +1 
		elif A[mid] > target:
			right = mid =1
		else:
			return mid
	return left
