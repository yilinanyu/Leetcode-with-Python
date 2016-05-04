class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) < 3:
            return []
        
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = i + 1
                r = len(nums) - 1
            
                while l < r:
                    tmp = nums[i] + nums[l] + nums[r]
                    if tmp == 0:
                        res.append((nums[i], nums[l], nums[r]))
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif tmp < 0:
                        l += 1
                    else:
                        r -= 1
        return res