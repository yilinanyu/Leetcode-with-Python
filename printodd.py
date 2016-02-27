def printodd(A):
	res = 0
	for i in A:
		res = res ^ i

	return res
print printodd([1,2,2,3,3])