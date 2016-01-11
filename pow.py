class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 递归
        if n == 0:
            return 1.0
        elif n < 0:
            return 1/self.myPow(x,-n)
        elif n % 2:
            return self.myPow(x*x,n/2)*x
        else:
            return self.myPow(x*x,n/2)