class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        res = 0
        nums.sort()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) -1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum < target:
                    res += r - l
                    l += 1
                else:
                    r -= 1
        return res
        