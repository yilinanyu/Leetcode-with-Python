def intersection(A, B):

	res = []
	m = len(A)
	n = len(B)
	i = 0
	j = 0
	res = []
	while i < m and j < n:
		if A[i] < B[j]:
			i += 1
		elif A[i] > B[j]:
			j += 1
		else:
			res.append(A[i])
			i += 1
			j += 1
		
	return res
A = [1,2,3,4,56]
B = [1,2]
print intersection(A, B)