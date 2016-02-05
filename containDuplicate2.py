# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
#[1,2,3,4,5,6,,7,2,3,4]
def containDuplicate(nums, k):
    numDict = dict()
    for x in range(len(nums)):
        # 去到x 的每一个index
        idx = numDict.get(nums[x])
        if idx > 0 and x - idx <= k:
            return True
        numDict[nums[x]] = x
    return False
nums = [1,2,3,4,1,3,4]
k = 2
print containDuplicate(nums, k)       

        
        
    
        