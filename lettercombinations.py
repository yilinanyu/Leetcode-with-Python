class Solution(object):
    # Time ; O(2^N)
    # space: O(N)
    def __init__(self):
            self.dic = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if digits is None or len(digits) == 0:
            return []
        # backtracking
        res = []
        line = []
        # digit from index 0
        self.helper(digits, 0, res, line)
        return res
        
    def helper(self, digits, cur, res, line):
        if len(line) == len(digits):
            # string to list 
            res.append("".join([x for x in line]))
            return
        for l in self.dic[digits[cur]]:
            line.append(l)
            # move to the next digits 
            self.helper(digits, cur+ 1, res, line)
            line.pop()
        
        