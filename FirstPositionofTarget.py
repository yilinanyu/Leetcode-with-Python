class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        left = 0; right = len(nums)
        while left +1 < right:
            mid = left + (right -left)/2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
        
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1