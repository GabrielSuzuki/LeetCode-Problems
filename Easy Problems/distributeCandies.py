class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        intDict = {}
        for i in candyType:
            if intDict.get(i) == None:
                intDict[i] = 1
            else:
                intDict[i] += 1
        total = 0
        for i in list(intDict.values()):
            total += i
        total /= 2
        count = 0
        for i in list(intDict.keys()):
            count += 1
            if total == count:
                return total
        return count