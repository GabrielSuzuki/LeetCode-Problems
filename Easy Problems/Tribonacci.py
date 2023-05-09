class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        tri = [0,1,1]
        if n == 0 or n == 1 or n == 2:
            return tri[n]
        for i in range(0,n-2):
            tri.append(tri[-1] + tri[-2] + tri[-3])
        return tri[-1]