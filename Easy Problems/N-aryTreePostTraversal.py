class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None:
            return []
        arr = [root.val]
        temp = []
        for i in root.children:
            temp += self.postorder(i)
        arr = temp + arr
        return arr