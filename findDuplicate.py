class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 1, len(nums)-1
        while low <= high:
            mid = (low+high)/2
            count = sum(x <= mid for x in nums)
            if count > mid:
                high = mid -1
            else:
                low = mid +1
        return low