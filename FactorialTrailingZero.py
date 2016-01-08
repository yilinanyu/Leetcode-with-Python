class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n! 后缀为0 的数= n! Prime factor中5 的个数 = 
        # floor (n/5) + floor (n/25) + floor(n/125)+..直到 n< 5N
        x = 5
        ans = 0
        while n >= x:
            ans += n/x
            x *= 5
        return ans