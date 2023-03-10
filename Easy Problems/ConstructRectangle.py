class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        L = 0
        W = 0
        tempArr = []
        if area == 1:
            return [1,1]
        if int(sqrt(area)) * int(sqrt(area)) == area:
            return [int(sqrt(area)), int(sqrt(area))]
        for i in range(1,area+1):
            if area % i == 0:
                tempArr.append(i)
        middle = len(tempArr) // 2 - 1
        i = middle
        j = middle + 1
        while i > -1 and j < len(tempArr):
            L = tempArr[j]
            W = tempArr[i]
            if L * W == area:
                return [L,W]
            i -= 1
            j += 1