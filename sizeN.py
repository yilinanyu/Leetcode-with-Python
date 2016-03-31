def sizeN(nums):
	if nums is None or len(nums) == 0 or len(nums) == 1:
		return None
	result = 0000000000
	for elem in nums:
		result[elem] += 1
	print result
	a = []
	for i in range(len(result)):
		if result[i] > 1:
			a.append(i)
	return a

print sizeN([1,2,2,3,4,4])
