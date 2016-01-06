class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 121
        # 1221
        # 2211
        # 不能使用额外空间，所以不能将数字转换成字符串来处理
        if x < 0:
            return False
        div = 1
        while x/div >= 10:
            div = div * 10
        
        while x:
            left = x/div 
            right = x % 10
            
            if left!= right:
                return False
            x = ( x % div ) / 10
            div = div / 100
        return True
        
        