# Devide and Conquer (general k sum question)
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) < 4:
            return []
        nums.sort()
        return [list(t) for t in self.kSum(nums, target, 4)]
    
    def kSum(self, nums, target, k):
        
        res = set()
        if k == 2:
            l = 0
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.add((nums[l], nums[r]))
                    l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            l = 0
            while l < len(nums) - k + 1:
                for n in self.kSum(nums[l + 1:], target - nums[l], k - 1):
                    res.add((nums[l],) + tuple(n))
                l += 1
        return res
                    
                
            
        