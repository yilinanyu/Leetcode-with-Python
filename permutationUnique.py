class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        nums.sort()
        res = []
        for i, x in enumerate(nums):
            if i == 0 or nums[i] != nums[i - 1]:
                for elem in self.permuteUnique(nums[:i] + nums[i+1:]):
                    res.append([x] + elem)
        return res
        
        