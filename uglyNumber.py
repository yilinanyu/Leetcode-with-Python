class Solution(object):
    def isUgly(self, num):
        # """
        # :type num: int
        # :rtype: bool
        # """
        # res = []
        # nums = [1,2,3,5]
        # for i in nums:
        #     for j in nums:
        #         res.append(i * j)
        # if num in res:
        #     return True
        # else:
        #将输入数不断除以x，当num ==1 时返回true 否则false
        if num <= 0:
            return False
        for x in [2, 3, 5]:
            while num % x == 0:
                num /= x
        return num == 1
