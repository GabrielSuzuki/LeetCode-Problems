import math
class Solution(object):
    def divisors(self,n):
        divs = [1]
        for i in xrange(2,int(math.sqrt(n))+1):
            if n%i == 0:
                divs.extend([i,n/i])
        return sum(list(set(divs)))
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return False
        if self.divisors(num) == num:
            return True
        else:
            return False