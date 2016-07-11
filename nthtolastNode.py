"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: Nth to last node of a singly linked list. 
    """
    def nthToLast(self, head, n):
        if head is None:
            return None
        k = self.length(head)
        n = n % k
        i = 0
        tmp = head
        while i < k - n:
            tmp = tmp.next
            i += 1
        return tmp.val
        
    def length(self, head):
        i = 0
        while head:
            head = head.next
            i += 1
        return i