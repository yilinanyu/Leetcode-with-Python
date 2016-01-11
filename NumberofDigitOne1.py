# First we divide the number into two parts: the left and the right. 

# If the last digit of left is larger than 1, then we have as many as (left/10 + 1) 1 as prefix
# If the last digit of left is smaller than 2, then there is only (left/10) 1 as prefix, plus the right part 
# class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        ones , m = 0, 1
        while m <= n:
            ones += (n/m + 8)/10 * m + (n/m %10 == 1) * (n % m + 1)
            m *= 10
        return ones