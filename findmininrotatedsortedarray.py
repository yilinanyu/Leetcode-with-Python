class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return None
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) / 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[r]