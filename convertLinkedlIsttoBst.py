# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def _init_(self):
        self.cur = None
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None or head.next is None:
            return head
        self.cur = head
        size = self.getSize(head)
        return self.myTree(size)
    def myTree(self,n):
        if n <= 0:
            return None
        l = self.myTree(n/2)
        root = TreeNode(self.cur.val)
        self.cur = self.cur.next
        r = self.myTree(n - n/2 - 1)
        root.left = l
        root.right = r
        return root
    def getSize(self,head):
        n = 0 
        while head:
            head = head.next 
            n += 1
        return n
        
        
        
     
        
        