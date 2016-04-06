# def findfirstdup(nums):
# 	for i in range(len(nums)):
# 		for j in range(i+1,len(nums)):
# 			if nums[i] == nums[j]:
# 				return nums[i]
# 	return None

# def findDup(nums):
# 	dict = {}
# 	for elem in nums:
# 		if elem in dict:
# 			return elem
# 		else:
# 			dict[elem] = 1
# 	return None

# print findDup([1,2,3,4,5,2])

def maparray(nums1, nums2):
	res = []
	for i in range(len(nums1)):
		for j in range(len(nums2)):
			return zip(nums1[i],nums2[j])
	return None
	# 		# return res
	# return Noness


print maparray([1,2],[2,3])