# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        # curr 表示移动的当前节点
        while curr.next:
            #如果curr.next < curr.val 即链表是升序的，curr 指针像后移动
            #直到一个节点的值，小于前面节点的值，然后寻找插入的位置
            if curr.next.val < curr.val:
                pre = dummy
                while pre.next.val < curr.next.val:
                    pre = pre.next
                #curr 指针向后移动
                tmp = curr.next
                curr.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                curr = curr.next
        return dummy.next 
        