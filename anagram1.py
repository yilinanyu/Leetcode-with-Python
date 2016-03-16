class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        # write your code here
        dict = {}
        for word in strs:
            sortedword = "".join(sorted(word))
            dict[sortedword] = [word] if sortedword not in dict else dict[sortedword] + [word]
            res = []
        for item in dict:
            if len(dict[item]) >= 2:
                res += dict[item]
        return res
        
        
        
        
        
        
        
        
        
        
        