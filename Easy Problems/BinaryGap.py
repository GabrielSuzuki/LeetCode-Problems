class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = str(bin(n))[2:]
        pos1 = 0
        currMax = 0
        for i in range(0,len(n)):
            if n[i] == '1':
                currMax = max(currMax,i-pos1)
                pos1 = i
        return currMax