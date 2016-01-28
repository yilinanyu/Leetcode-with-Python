# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # if headA is None or headB is None:
        #     return None
        # if id(headA) == id(headB) and headA.next is None and headB.next is None:
        #     return headA
        # idea: move the longer headX A-B steps so that they can be in the same start point. Thus when id (headA) == id(headB): the intersection will be headA(B)
        m = self.getSize(headA)
        n = self.getSize(headB)
        # we have to ensure the longer list moves 
        if m > n:
            for i in range (m - n):
                headA = headA.next
        else:
            for i in range(n - m):
                headB = headB.next
        
        while headA and headB:
            if id(headA) == id(headB):
                return headA
            headA = headA.next
            headB = headB.next
        return None
    
    def getSize(self, head):
        k = 0 
        while head:
            head = head.next 
            k +=1 
        return k
        
        
            
            
        