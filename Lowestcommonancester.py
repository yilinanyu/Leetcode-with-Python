


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # if we can not find this node or node is None return none
        if not root:
            return None
        # if my node equals to p or q, we return root, means we find it 
        if root == p or root == q:
            return root
        # the find result in lca in left is the way we find in the left root of the root
        # same as right.
        # if we find one, return the root, if not return none
        lca_in_left = self.lowestCommonAncestor(root.left, p, q)
        lca_in_right = self.lowestCommonAncestor(root.right, p, q)
        # if right and left both find, which means, one node is in left site and other one is in right site, in this case, return lca is the root
        if lca_in_right and lca_in_left:
            return root
        # otherwise, we found at left and return node at right site, which mean two nodes are at the same sites. in this case, return the l
        return lca_in_left or lca_in_right
        