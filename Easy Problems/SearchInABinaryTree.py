class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return root
        if root.val == val:
            return root
        return self.searchBST(root.left,val) or self.searchBST(root.right,val)