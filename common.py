def printCommon(num1, num2):
	if num1 is None or num2 is None:
		print None
	res = []
	for i in range(len(num1)):
		for j in range(len(num2)):
			if num1[i] == num2[j]:
				res.append(num1[i])
	return res
print printCommon([1,2,3],[3,4])

