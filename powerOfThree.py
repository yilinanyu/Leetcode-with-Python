class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # while n != 1:
        #     if n % 3 == 0:
        #         n /=3
        #     else:
        #         return False
        # return True
        #I : one line code
        # return n>0 and 3**round(math.log(n,3)) == n
        #II: recursion
        if n == 1:
            return True
        if n == 0 or n%3 > 0:
            return False
        return self.isPowerOfThree(n/3)
        