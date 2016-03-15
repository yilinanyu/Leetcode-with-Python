class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    # O(log n)
    def binarySearch(self, nums, target):
        if len(nums) == 0:
            return -1
            
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
                
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1