class Solution(object):
    def BST(self, valString, root):
        if root.left == None and root.right == None:
            return int("0b" + valString + str(root.val),2)
        elif root.left == None and root.right != None:
            return self.BST(valString+str(root.val),root.right)
        elif root.left != None and root.right == None:
            return self.BST(valString+str(root.val),root.left)
        else:
            return self.BST(valString+str(root.val),root.right) + self.BST(valString+str(root.val),root.left)

    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return self.BST("",root)