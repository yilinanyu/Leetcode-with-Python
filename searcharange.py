class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.helper(nums, target)
        if left < len(nums) and nums[left] == target:
            right = self.helper(nums, target + 1) - 1
            return [left, right]
        else:
            return [-1, -1]
    def helper(self, nums, target):
        l = 0
        r = len(nums)
        while l < r:
            mid = l + (r - l) / 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l 
                
                
                
                
                
                