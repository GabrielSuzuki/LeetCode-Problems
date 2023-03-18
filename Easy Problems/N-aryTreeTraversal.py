class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None:
            return []
        arr = [root.val]
        for i in root.children:
            arr += self.preorder(i)
        return arr