class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0 
        r = len(height) - 1
        water = 0
        while l < r and height[l] < height[l + 1]:
            l += 1
        while l < r and height[r] < height[r - 1]:
            r -= 1
        while l < r:
            leftheight = height[l]
            rightheight = height[r]
            
            if leftheight < rightheight:
                while l < r and height[l] <= leftheight:
                    water += leftheight - height[l]
                    l += 1
            else:
                while l < r and height[r] <= rightheight:
                    water += rightheight - height[r]
                    r -= 1
        return water
            
        
        
        