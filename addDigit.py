class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = 0
        while(num):
            res = 0
            for i in range(len(str(num))):
                res = res + int(str(num)[i])
            if len(str(res))>1:
                num = res
            else:
                break
        return res
        