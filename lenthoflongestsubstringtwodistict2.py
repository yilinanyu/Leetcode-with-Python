class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstringTwoDistinct(self, s):
        counts = [0] * 256
        i = maxLen = numChar = 0
        
        for j in range(len(s)):
            if counts[ord(s[j])] == 0:
                numChar += 1
            
            counts[ord(s[j])] += 1
            
            while i < len(s) and numChar > 2:    # more than 2 distinct in the window
                counts[ord(s[i])] -= 1
                if counts[ord(s[i])] == 0:      
                    numChar -= 1
                i += 1
            
            maxLen = max(maxLen, j - i + 1)      # get the max value each time
            
        return maxLen