class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 1
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l) / 2
            count = 0
            for x in nums:
                if x >= l and x <= mid:
                    count += 1
            if count > mid - l + 1:
                r = mid
            else:
                l = mid + 1
        return r