class Solution(object):
#     Take aabbbcc as an example

# counter would be {"a":2, "b":3, "c":2}

# After preprocess: baseStr = "abc", mid = "b" (if there is no char happens odd times, mid = "")

# Then use backtracking to find all the permutation of baseStr,

# the valid palindrome would be "permuStr + mid + reverseOfPermuStr"
    def generatePalindromes(self, s):
        counter = collections.Counter(s)
        odds = filter(lambda x: x % 2, counter.values())
        if len(odds) > 1:
            return []
        baseStr, mid = self.preProcess(counter)
        return self.backTracking(baseStr, 0, mid, [baseStr + mid + baseStr[::-1]])

    def preProcess(self, counter):
        baseStr = mid = ""
        for char in counter:    
            if counter[char] % 2:
                mid = char
            baseStr += char*(counter[char]/2)
        return baseStr, mid

    def backTracking(self, s, idx, mid, ans):
        if idx == len(s) - 1:
            return ans
        for i in range(idx, len(s)):
            if i >= 1 and s[i] == s[i-1] == s[idx]:
                continue #no need to go deeper if swap would be the same
        #Swap s[idx] with s[i]
            if i != idx:
                permu = s[:idx] + s[i] + s[idx+1:i] + s[idx] + s[i+1:] 
                ans.append(permu + mid + permu[::-1])
            else:
                permu = s
            self.backTracking(permu, idx+1, mid, ans)
        return ans
        