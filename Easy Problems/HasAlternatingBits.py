class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binNum = str(bin(n))
        for i in range(1,len(binNum)):
            if binNum[i] == binNum[i-1]:
                return False
        return True