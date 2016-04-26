class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l)/2
            if (mid == 0 or nums[mid] > nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] > nums[mid + 1]):# 注意判断mid 为第一个值和最后一个值的条件
                return mid
            elif mid > 0 and nums[mid] < nums[mid - 1]:# 注意 mid > 0 的条件
                r = mid - 1
            else:
                l = mid + 1
        return -1
                
        