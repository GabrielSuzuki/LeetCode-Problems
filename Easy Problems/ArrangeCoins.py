class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        rowNum = 1
        while rowNum <= n:
            n -= rowNum
            rowNum += 1
        return rowNum - 1