class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        n = len(s)
        
        l = 0
        r = n - 1
        
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            
            while l < r and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
       
        return True