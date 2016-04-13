# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Time: O(Nk)
    # Space：O(N)
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n = len(lists)
        if not list or n == 0:
            return None
        elif n == 1:
            return lists[0]
        elif n == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        else:
            mid = n/2
            return self.mergeKLists([self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])])
    
    def mergeTwoLists(self, l1, l2):
        cur = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
            else:
                cur.next = l2
                l2 = l2.next
                cur = cur.next

        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next
        
        