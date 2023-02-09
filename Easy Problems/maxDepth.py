class Solution(object):
    def inOrder(self,root,count):
        count += 1
        if root.left == None and root.right == None:
            return count
        if root.left == None and root.right != None:
            return self.inOrder(root.right,count)
        elif root.right == None and root.left != None:
            return self.inOrder(root.left,count)
        else:
            left = self.inOrder(root.left,count)
            right = self.inOrder(root.right,count)
            if left > right:
                return left
            else:
                return right
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = 0
        if root == None:
            return 0
        return self.inOrder(root,count)