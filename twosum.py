class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [i, dict[target - nums[i]]]
            dict[nums[i]] = i
        return []
