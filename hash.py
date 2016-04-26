def printCommon(num1, num2):
	if num1 is None or num2 is None:
		print None
	nums1 = set(num1)
	nums2 = set(num2)
	res = []
	for i in nums1:
		if i in nums2:
			res.append(i)
	return res
print printCommon([1,4,3],[3,4])

