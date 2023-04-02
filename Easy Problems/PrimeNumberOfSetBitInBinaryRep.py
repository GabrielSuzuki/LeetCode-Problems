class Solution(object):
    def is_prime(self,n):
        if n < 2: 
            return False
        if n % 2 == 0:             
            return n == 2  # return False
        k = 3
        while k*k <= n:
            if n % k == 0:
                return False
            k += 2
        return True
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        countBits = 0
        total = 0
        for i in range(left,right+1):
            countBits = 0
            newBit = str(bin(i))
            for j in range(0, len(newBit)):
                if newBit[j] == '1':
                    countBits += 1
            if self.is_prime(countBits):
                total += 1
        return total