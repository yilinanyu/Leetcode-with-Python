class Solution(object):
    def twoSum(self, num, target):
        # define a nil dictionary 
     dict = {}
     for i in range(len(num)):
         x = num[i]
         if target-x in dict:
             return (dict[target-x]+1,i+1)
         dict[x]=i
