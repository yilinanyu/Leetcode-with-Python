def intersection(A,B):
	hashset = set(A)
	for i in range(len(B)):
		if B[i] in hashset:
			res.append(B[i])
		else:
			continue
	return res
