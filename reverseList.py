# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def reverseList(self, head):
        curt = None
        while head!= None:
            temp = head.next
            head.next = curt
            curt = head
            head = temp
        return curt
        