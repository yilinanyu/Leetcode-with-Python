class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = 0; R = len(nums)-1
        while L < R and nums[L]>=nums[R]:
            M = (L+R)/2
            if nums[M] > nums[L]: 
                L= M+1
            elif nums[M] < nums[R]: 
                R = M
            else: 
                L +=1 
        return nums[L]