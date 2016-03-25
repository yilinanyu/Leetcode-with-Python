class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        res = ''.join(self.quicksort(map(str, nums))).lstrip('0')
        
        if len(res) == 0:
            return '0'
        else:
            return res
        
    def quicksort(self, nums):
        if len(nums) <= 1:
            return nums
        
        i = 0
        j = len(nums) - 1
        
        while i < j:
            if nums[i] + nums[i + 1] < nums[i + 1] + nums[i]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                i += 1
            else:
                nums[i + 1], nums[j] = nums[j], nums[i + 1]
                j -= 1
            
        return self.quicksort(nums[:i]) + [nums[i]] + self.quicksort(nums[i + 1:])