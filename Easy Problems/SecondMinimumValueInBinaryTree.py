class Solution(object):
    def BST(self,root):
        if root == None:
            return []
        return [root.val] + self.BST(root.left) + self.BST(root.right)
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sortedList = []
        sortedList = sorted(self.BST(root))
        firstMin = sortedList[0]
        for i in range(1,len(sortedList)):
            if sortedList[i] != firstMin:
                return sortedList[i]
        return -1