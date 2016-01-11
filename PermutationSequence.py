# Let num = [1,2,3,...,n]. The first digit is k/(n-1)!, then let k = k % (n-1)! and remove this digit from num. The second digit is k/(n-2)!, then let k = k % (n-2)! and remove this digit from num and so on.

class Solution:
    # @return a string
    def getPermutation(self, n, k):
        res = ''
        k -= 1 # count from 0
        factorial = 1
        for i in xrange(1, n):
            factorial *= i
        num = [i for i in xrange(1, n + 1)]
        for i in reversed(xrange(n)):
            curr = num[k / factorial]
            res += str(curr)
            num.remove(curr)
            if i != 0:
                k %= factorial
                factorial /= i
        return res