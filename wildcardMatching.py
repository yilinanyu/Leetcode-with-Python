class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    # @good solution! use 'aaaabaaaab' vs 'a*b*b' as an example
    def isMatch(self, s, p):
        pPointer=sPointer=ss=0; star=-1
        while sPointer<len(s):
            if pPointer<len(p) and (s[sPointer]==p[pPointer] or p[pPointer]=='?'):
                sPointer+=1; pPointer+=1
                continue
            if pPointer<len(p) and p[pPointer]=='*':
                star=pPointer; pPointer+=1; ss=sPointer;
                continue
            if star!=-1:
                pPointer=star+1; ss+=1; sPointer=ss
                continue
            return False
        while pPointer<len(p) and p[pPointer]=='*':
            pPointer+=1
        if pPointer==len(p): return True
        return False