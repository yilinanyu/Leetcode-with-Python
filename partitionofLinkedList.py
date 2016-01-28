# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        head1 = ListNode(0)
        head2 = ListNode(0)
        Tmp = head
        phead1 = head1
        phead2 = head2
        while Tmp:
            if Tmp.val < x:
                phead1.next = Tmp
                Tmp = Tmp.next
                phead1 = phead1.next
                phead1.next = None
            else:
                phead2.next = Tmp
                Tmp = Tmp.next
                phead2 = phead2.next
                phead2.next = None
        phead1.next = head2.next
        head = head1.next
        return head