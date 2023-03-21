class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        nTotal = 0
        if n == 0:
            return True
        for i in range(0,len(flowerbed)):
            if flowerbed[i] == 0:
                if i-1 < 0 or flowerbed[i-1] == 0:
                    if i+1 > len(flowerbed)-1 or flowerbed[i+1] == 0:
                        nTotal += 1
                        flowerbed[i] = 1
                        if nTotal == n:
                            return True
        return False 