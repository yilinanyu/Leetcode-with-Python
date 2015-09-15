class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {x: False for x in nums}
        maxLen = -1
        for i in dict:
            if dict[i] == False:
                curr= i+1; lenright = 0
                while curr in dict:
                    lenright+=1; dict[curr] = True; curr+=1
                curr = i-1; lenleft = 0
                while curr in dict:
                    lenleft+=1; dict[curr] = True; curr-=1
                maxLen = max(lenleft+lenright+1,maxLen)
        return maxLen
                
        