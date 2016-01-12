class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # 滑动 窗口的方法 sliding window
        size = len(nums)
        start, end, sum = 0, 0, 0
        bestAns = size + 1
        while end < size:
            while end < size and sum < s:
                sum += nums[end]
                end +=1
            while start < end and sum >= s:
                bestAns = min(bestAns, end - start)
                sum -= nums[start]
                start += 1
                
        return [0, bestAns][bestAns <= size]
                