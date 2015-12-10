class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #exclusive or是对两个运算元的一种逻辑分析类型，符号为XOR或EOR或⊕
        ans = nums[0]
        for i in range(1, len(nums)):
            ans = ans ^ nums[i]
        return ans
        