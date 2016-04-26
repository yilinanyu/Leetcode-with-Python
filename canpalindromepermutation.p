class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                
        already = False
        for i in d:
            if d[i] % 2 != 0:
                if already:
                    return False
                else:
                    already = True
        return True

        