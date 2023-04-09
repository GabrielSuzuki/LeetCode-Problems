# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def BST(self,root):
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.val]
        return self.BST(root.left) + self.BST(root.right)
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if self.BST(root1) == self.BST(root2):
            return True
        else:
            return False