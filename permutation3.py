class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
   
        # time complexity: O(n!) N factory
        # 3 times 2 
        #backtracking:
        if len(nums) <= 1:
            return [nums]
        res = []
        for i, x in enumerate(nums):
	    	# 1 and two subarray
            # 1->[2,3],[3,2]
            # 2->[1,3],[3,1]
		    # recurssion to 2 in the second place and 3 in the scond place
		    # elem equals except the x emit the nums[i]
		    for elem in self.permutate(nums[:i]+ nums[i+1:]):
		        res.append([x] + elem)
		
		
		
		return res