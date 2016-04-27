class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None:
            return None
        l = 0
        # 注意r = len(nums) 因为有可能找不到此值 如[1,3,5,6], 7 → 4
        r = len(nums)
        while l < r:
            mid = l + (r - l)/2
            if nums[mid] >= target:
                r = mid 
            else:
                l = mid + 1
        return l
        