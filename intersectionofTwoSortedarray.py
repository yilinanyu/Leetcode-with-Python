def intersection(num1, num2):
	if num1 is None or num2 is None:
		return None
	res = []
	i = 0
	j = 0
	while i < len(num1) and j < len(num2):
		if num1[i] < num2[j]:
			i += 1
		elif num1[i] > num2[j]:
			j += 1
		else:
			res.append(num1[i])
			i += 1
			j += 1
	return res
print intersection([2,3,4,5,6], [2,3,4,5,6])