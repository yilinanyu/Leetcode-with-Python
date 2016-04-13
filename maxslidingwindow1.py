class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        deque = collections.deque()
        ans = []
        for i in range(len(nums)):
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()
            deque.append(i)
            if i - deque[0] == k:
                deque.popleft()
            if i >= k - 1:
                ans.append(nums[deque[0]])
        return ans
                
        