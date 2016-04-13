class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if not nums or n == 0:
            return 0
        dp = [0] *n
        dp [0] = maxSub = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i -1] + nums[i], nums[i])
            maxSub = max(dp[i], maxSub)
        return maxSub