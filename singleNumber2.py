class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        ans = 0
        
        for i in range(32):
            count = 0
            for j in nums:
                if j >> i & 1:
                    count += 1
            if count % 3 == 1:
                ans |= 1 << i
        
        if ans >= 2 ** 31:
            ans -= 2 ** 32
        return ans