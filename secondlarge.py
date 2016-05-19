# def findsecond(nums):
# 	nums.sort()
# 	print nums[len(nums) - 2]
# #A Simple Solution is to sort the array in increasing order.
# # The first two elements in sorted array would be two smallest elements. 
# #Time complexity of this solution is O(n Log n).
# nums = [1,2,3,4,5,2,1]
# findsecond(nums)

# A Better Solution is to scan the array twice. 
# In first traversal find the minimum element. Let this element be x. 
# In second traversal, find the smallest element greater than x. Time complexity of this solution is O(n).
# The above solution requires two traversals of input array.


# An Efficient Solution can find the minimum two elements in one traversal. Below is complete algorithm.

# Algorithm: O(N)

# 1) Initialize both first and second smallest as INT_MAX
#    first = second = INT_MAX
# 2) Loop through all the elements.
#    a) If the current element is smaller than first, then update first 
#        and second. 
#    b) Else if the current element is smaller than second then update 
#     second

def print2Smallest(arr):
 
    # There should be atleast two elements
    arr_size = len(arr)
    if arr_size < 2:
        print "Invalid Input"
        return
 
    first = second = float("inf")
    for i in range(0, arr_size):
 
        # If current element is smaller than first then
        # update both first and second
        if arr[i] < first:
            second = first
            first = arr[i]
 
        # If arr[i] is in between first and second then
        # update second
        elif (arr[i] < second and arr[i] != first):
            second = arr[i];
    return second


print print2Smallest([0,2,3,4,2,1,1,-1,3])