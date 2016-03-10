class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        oldStr = "1"
        
        for i in range(n - 1):
            newStr = ""
            count = 1
            for i in range(1, len(oldStr) + 1):
                if i == len(oldStr) or (oldStr[i] != oldStr[i - 1]):
                    newStr += str(count) + oldStr[i - 1]
                    count = 1
                else:
                    count += 1
            
            oldStr = newStr
        
        return oldStr