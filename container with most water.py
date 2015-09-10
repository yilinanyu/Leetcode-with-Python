class Solution:
    # @return an integer
    def maxArea(self, height):
        left = 0; right = len(height)-1
        res = 0
        while left < right:
            water = min(height[left], height[right]) * (right-left)
            if water > res: res = water
            if height[left] < height[right]: 
                left += 1
            else:
                right -= 1
        return res