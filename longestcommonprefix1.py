class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix
    def longestCommonPrefix(self, strs):
        # write your code here
        if strs is None or len(strs) == 0:
            return ""
        prefix = strs[0]
        
        for i in range(1,len(strs)):
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            prefix = prefix[:j]
        return prefix
                    