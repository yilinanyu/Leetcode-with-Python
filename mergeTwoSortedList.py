# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    # we don't know which to start, we nend dummy node dummy is for where to start
    #cur node like the pointer its dynamic.
    dummy = cur = ListNode(0)
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
                
        
        