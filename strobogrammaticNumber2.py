class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # list 列表 数据结构
        nums = n%2 * list('018') or ['']
        #nums = []
        while n > 1:
            n -= 2
            nums = [a  + num + b for a, b in '00 11 88 69 96'.split()[n<2:] for num in nums]
        return nums
            
        