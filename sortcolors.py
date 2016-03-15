class Solution(object):
    # 0 1 111 222 000 111
    # 0000 (red )1111111 222(blue)
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red = 0

        blue = len(nums) - 1
        i = 0
        while i <= blue:
            if nums[i] == 0:
                nums[i], nums[red] = nums[red], nums[i]
                red += 1
            elif nums[i] == 2:
                nums[i], nums[blue] = nums[blue] , nums[i]
                blue -= 1
                # 换过来的数 从后面来的，并不能确定他的值，需要blue 向前一步
                i -= 1
            i += 1 
            
        
        
        