def findfirstDuplicate(nums):
	dict = {}
	for i in range(len(nums)):
		x = nums[i]
		if nums[i] in dict:
			return nums[i]
		dict[x] = i
print findfirstDuplicate([1,3,0,0,3,2,1])
