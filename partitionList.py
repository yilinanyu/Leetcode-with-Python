# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        #解决链表问题，最好加一个头结点，对于这个问题，创建两个头结点，head1 and head2. head1 是小于x 值的节点的链表，head2 是大于等于x值的节点的链表。然后将head2 加到head1 的尾部即可。
        head1 = ListNode(0)
        head2 = ListNode(0)
        tmp = head
        phead1 = head1
        phead2 = head2
        #看我怎么给他们分开啊 
        while tmp:
            # deal with head1 smaller than x
            if tmp.val < x:
                phead1.next = tmp
                tmp = tmp.next
                phead1 = phead1.next
                phead1.next = None
            else:
                phead2.next = tmp
                tmp = tmp.next
                phead2 = phead2.next
                phead2.next = None
        #merge two phead
        phead1.next = head2.next
        # define the head equels to head1
        head = head1.next
        return head
        