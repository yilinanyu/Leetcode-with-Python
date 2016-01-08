import sys
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        answer = 0
        if x >= sys.maxint or x<-sys.maxint:
            return 0
        elif sys.maxint> x >0:
            sign = 1
        else:
            sign = -1
        x = abs(x)
        while x > 0:
            if answer*10.0 + x%10 > 2147483647:return 0
            answer = answer * 10 + x % 10
            x /= 10
        return sign*answer

