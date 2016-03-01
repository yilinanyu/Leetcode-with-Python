class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {"(":")","{":"}","[":"]"}
        stack = []
        for c in s:
            if c in dict:
                stack.append(c)
            else:
                if not stack or dict[stack.pop()] != c:
                    return False
        return not stack
            
        