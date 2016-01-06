class Solution:
    # from discussion at leetcode 
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        # 当其中一个为空
        if headA is None or headB is None:
            return None
        # define pointera and pointerb
        pa = headA # 2 pointers
        pb = headB

        # 当pa 不等于pb 即他俩没有相遇的时候
        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal, 
            # if not hit the end, just move on to next
            # 如果到头了就换另一个，没有的话就继续
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa # only 2 ways to get out of the loop, they meet or the both hit the end=None

# the idea is if you switch head, the possible difference between length would be countered. 
# On the second traversal, they either hit or miss. 
# if they meet, pa or pb would be the node we are looking for, 
# if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None