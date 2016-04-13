class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """ 
        # O(N) time and O(1) space
        # Modify: shift = 0 
        # abcde
        # abXde
        # Insertion: shift = 1
        # abcde
        # abXcde
        # Append shift = 1
        # abcde
        # abcdeX
        # Identical
        # abcde
        # abcde shift = 0
        m = len(s)
        n = len(t)
        if m > n:
            return self.isOneEditDistance(t,s)
        if n - m > 1:
            return False
        index = 0
        shift = n - m# shift = 0 or shift = 1
        while index < m and s[index] == t[index]:
            index += 1
        if index == m:
            return shift > 0
        # jump situation
        if shift == 0:
            index += 1
        while index < m and s[index] == t[index + shift]:
            index += 1
        return index == m
        
            
        
            