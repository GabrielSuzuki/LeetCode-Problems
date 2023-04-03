class Solution(object):
    def BST(self,root):
        if root == None:
            return []
        return self.BST(root.left) + [root.val] + self.BST(root.right)
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        newArr = sorted(self.BST(root))
        minimum = newArr[1] - newArr[0]
        for i in range(2,len(newArr)):
            minimum = min(minimum,newArr[i] - newArr[i-1])
        return minimum