# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def finder(self,root):
        if root == None:
            return None
        temp = TreeNode(root.val,self.finder(root.right),self.finder(root.left))
        return temp
            

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        temp = root
        if root == None:
            return None
        if root.left == None and root.right == None:
            return root
        reverse = root
        reverse = self.finder(root)
        return reverse