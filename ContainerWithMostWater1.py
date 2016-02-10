class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        取最大最小的情况 用二分法
        """
        l = 0
        r = len(height) - 1
        res = 0
        if height is None or len(height) == 0:
            return None
        while l < r:
            res = max(res, (r - l) * min(height[l], height[r]))
            # 既然改变不了要移动的事实，就只能移动较小的棍子
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
                
              
        
        
        