
def inOrderSuccessor(root):
	# Time Complexity: O(h) where h is height of tree.
# if right is none, 
# 2) If right sbtree of node is NULL, then succ is one of the ancestors. 
# Travel up using the parent pointer until you see a node which is left child of it’s parent.
# The parent of such a node is the suc
if root.right is None:
    curr = root.parent
    while curr.key < root.key and curr != null:
        curr = curr.parent
    return curr
 # if right subtree is not null, find the min of my right sub tree
#If right subtree of node is not NULL, then succ lies in right subtree. Do following.
# Go to right subtree and return the node with minimum key value in right subtree.
 else:
     curr = root.right
     while curr.left is not None:
         curr = curr.left
     return curr

def inorderSuccessor(self, root, p):

# 	The inorder traversal of a BST is the nodes in ascending order. 
#To find a successor, you just need to find the smallest one that is larger than the given value since there are no duplicate values in a BST.
# It just like the binary search in a sorted list. 
#The time complexity should be O(h) where h is the depth of the result node. succ is a pointer that keeps the possible successor. 
#Whenever you go left the current root is the new possible successor, otherwise the it remains the same.
# 1) If right subtree of node is not NULL, then succ lies in right subtree. Do following.
# Go to right subtree and return the node with minimum key value in right subtree.
# 2) If right sbtree of node is NULL, then start from root and us search like technique. Do following.
# Travel down the tree, if a node’s data is greater than root’s data then go right side, otherwise go to left side.

# Only in a balanced BST O(h) = O(log n). In the worst case h can be as large as n.
    succ = None
    while root:
        if p.val < root.val:
            succ = root
            root = root.left
        else:
            root = root.right
    return succ
# iteratively, O(k)
def inorderSuccessor3(self, root, p):
    stack, res = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return 
        node = stack.pop()
        res.append(node)
        if len(res) > 1 and res[-2] == p:
            return res[-1]
        root = node.right

