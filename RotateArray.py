class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 空间复杂度O（n）
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]