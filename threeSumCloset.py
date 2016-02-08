class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return None
        
        nums.sort()
        res = 2147383647
        
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if abs(tmp - target) < abs(res - target):
                    res = tmp
                if tmp == target:
                    return tmp
                elif tmp < target:
                    l += 1
                else:
                    r -= 1
        return res
                    
        