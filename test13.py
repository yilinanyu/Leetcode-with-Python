class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # remove or change the parentheses one by one, BFS
        queue = {s}
        while True:
            valid = self.filtercheck(queue)
            if valid:
                return valid
            queue = {s[:i]+ s[i+1:] for s in queue  for i in range(len(s))} 
    
    def filtercheck(self,A):
        res = []
        for word in A:
            left = 0
            for c in word:
                if c == "(":
                    left += 1
                if c == ")":
                    left -= 1
                    if left < 0:
                        break
            if left == 0:
                res.append(word)
        return res
                
        
        
        