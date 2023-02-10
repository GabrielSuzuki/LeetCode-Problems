class Solution(object):
    def checkSum(self,root,targetSum,total):
        total += root.val
        if root.left == None and root.right == None:
            if total == targetSum:
                return True
            else:
                return False
        if root.left != None:
            left = self.checkSum(root.left,targetSum,total)
            if left == True:
                return True
        if root.right != None:
            right = self.checkSum(root.right,targetSum,total)
            if right == True:
                return True
        return False
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
        if root == None:
            return False
        total = root.val
        if root.left == None and root.right == None:
            if total == targetSum:
                return True
            else:
                return False
        if root.left != None:
            left = self.checkSum(root.left,targetSum,total)
            if left == True:
                return True
        if root.right != None:
            right = self.checkSum(root.right,targetSum,total)
            if right == True:
                return True
        return False