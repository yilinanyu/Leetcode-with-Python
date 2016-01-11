class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #实现开平方函数。这里要注意的一点是返回的时一个整数。通过这一点我们可以看出，很有可能是使用二分查找来解决问题的。这里要注意折半查找起点和终点的设置。起点i=1；终点j=x/2+1；因为在(x/2+1)^2 > x，所以我们将折半查找的终点设为x/2+1。
        if x == 0:
            return 0
        i = 1; j = x/2 + 1
        while (i<=j):
            center = ( i + j )/2
            if center**2 == x:
                return center
            elif center ** 2 > x:
                j = center - 1
            else:
                i = center + 1
        return j
        