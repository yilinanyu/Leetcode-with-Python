class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 等差数列求和公式 啊嘎嘎嘎嘎
        n = len(nums)
        return n*(n+1)/2 - sum(nums)