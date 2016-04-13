class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"M":1000, "D": 500, "C": 100,"L":50, "X":10, "V": 5, "I":1}
        result = d[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            if d[s[i]] < d[s[i + 1]]:
                result -= d[s[i]]
            else:
                result += d[s[i]]
        return result
         