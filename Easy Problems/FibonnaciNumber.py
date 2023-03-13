class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        first = 0
        second = 1
        temp = 0
        for i in range(2,n+1):
            temp = first + second
            first = second
            second = temp
        return second