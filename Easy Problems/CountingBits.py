class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arrTotal = []
        for i in range(n+1):
            arrTotal.append(bin(i).count("1"))
        return arrTotal